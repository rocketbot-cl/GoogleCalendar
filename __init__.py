# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os.path
import sys

PrintException = PrintException # type: ignore
GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'GoogleCalendar' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if cur_path_x64 not in sys.path and sys.maxsize > 2**32:
    sys.path.append(cur_path_x64)
elif cur_path_x86 not in sys.path and sys.maxsize > 32:
    sys.path.append(cur_path_x86)

from googleapiclient import discovery #type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from openpyxl.utils.cell import column_index_from_string, get_column_letter

import traceback
import pickle
import re

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

global creds
global mod_gcal_session

session = GetParams("session")
if not session:
    session = ''
    
try:
    if not mod_gcal_session : #type:ignore
        mod_gcal_session = {}
except NameError:
    mod_gcal_session = {}

if module == "GoogleSuite":
    cred = None
    credential_path = GetParams("credentials_path")
    port = 8080 if not GetParams("port") else GetParams("port")

    if session == '':
        filename = "token_calendar.pickle"
    else:
        filename = "token_calendar_{s}.pickle".format(s=session)
    
    filename = os.path.join(base_path, filename)
    
    try:
        if not os.path.exists(credential_path):
            raise Exception(
                "El archivo de credenciales no existe en la ruta especificada")

        SCOPES = [
            'https://www.googleapis.com/auth/calendar',
            'https://www.googleapis.com/auth/calendar.events',
            'https://www.googleapis.com/auth/calendar.addons.execute'
        ]

        if os.path.exists(filename):
            with open(filename, 'rb') as token:
                cred = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credential_path, SCOPES)
                cred = flow.run_local_server(port=port)
            # Save the credentials for the next run
            with open(filename, 'wb') as token:
                pickle.dump(cred, token)
        
        # global creds
        mod_gcal_session[session] = cred
        
    except Exception as e:
        traceback.print_exc()
        PrintException()
        raise e

if not mod_gcal_session[session]:
    raise Exception("There's no credentials, nor valid token. Please, generate your credentials.")

if module == "ListCalendars":

    result = GetParams('result')

    service = discovery.build('calendar', 'v3', credentials=mod_gcal_session[session])

    request = service.calendarList().list()
    response = request.execute()
    calendars = []
    for calendar in response["items"]:
        cal = {
            "id": calendar["id"],
            "name": calendar["summary"],
            "description": calendar.get("description",""),
            "primary": calendar.get("primary", False),
            "accessRole": calendar.get("accessRole", "")
        }
        calendars.append(cal)
    if result:
        SetVar(result, calendars)

if module == "ListEvents":
    calendarId = GetParams('calendarId')
    result = GetParams('result')

    service = discovery.build('calendar', 'v3', credentials=mod_gcal_session[session])

    page_token = None
    events = []
    while True:
        response = service.events().list(calendarId=calendarId, pageToken=page_token).execute()
        for event in response['items']:
            event_ = {
                "id": event["id"],
                "summary": event.get("summary",""),
                "status": event.get("status",""),
                "creator": event.get("creator",""),
                "organizer": event.get("organizer",""),
                "attendees": event.get("attendees",""),
                "start": event.get("start",""),
                "end": event.get("end",""),
                "hangoutLink": event.get("hangoutLink",""),
            }
            events.append(event_)
        page_token = response.get('nextPageToken')
        if not page_token:
            break

    if result:
        SetVar(result, events)

if module == "GetEvent":
    eventId = GetParams('eventId')
    calendarId = GetParams('calendarId')
    notify = GetParams("notify")    
    result = GetParams('result')

    service = discovery.build('calendar', 'v3', credentials=mod_gcal_session[session])
    request = service.events().get(calendarId=calendarId, eventId=eventId)
    response = request.execute()

    try:
        if result:
            SetVar(result, response)
    except Exception as e:
        if result:
            SetVar(result, False)
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e
   
if module == "CreateEvent":
    calendarId = GetParams('calendarId')
    notify = GetParams("notify")
    summary = GetParams("summary")
    location = GetParams("location")
    description = GetParams("description")
    start_dateTime = GetParams("start_dateTime")
    start_timeZone = GetParams("start_timeZone")
    end_dateTime = GetParams("end_dateTime")
    end_timeZone = GetParams("end_timeZone")
    recurrence = GetParams("recurrence")
    attendees = GetParams("attendees")
    reminders = GetParams("reminders")
    
    if notify:
        notify = eval(notify)
        if notify:
            notify = "all"
    else:
        notify = "none"
    
    result = GetParams('result')
    body_ = {}
    if summary:
        body_['summary'] = summary
    if location:
        body_['location'] = location
    if description:
        body_['description'] = description
    if start_dateTime and start_timeZone:
        body_['start'] = {
            'dateTime': start_dateTime,
            'timeZone': start_timeZone,
        }
    if end_dateTime and end_timeZone:
        body_['end'] = {
            'dateTime': end_dateTime,
            'timeZone': end_timeZone,
        }
    if recurrence:
        body_['recurrence'] = recurrence
    if attendees:
        body_['attendees'] = [{'email': email} for email in attendees]
    if reminders:
        body_['reminders'] = {
            'useDefault': False,
            'overrides': reminders
        }

    service = discovery.build('calendar', 'v3', credentials=mod_gcal_session[session])

    request = service.events().insert(calendarId=calendarId, sendUpdates=notify , body=body_)
    response = request.execute()

    try:
        if result:
            SetVar(result, True)
    except Exception as e:
        if result:
            SetVar(result, False)
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "UpdateEvent":
    body_ = GetParams('body')
    calendarId = GetParams('calendarId')
    eventId = GetParams('eventId')
    notify = GetParams("notify")
    result = GetParams('result')
    
    if body_:
        body_ = eval(body_)
    
    if notify:
        notify = eval(notify)
        if notify:
            notify = "all"
    else:
        notify = "none"

    service = discovery.build('calendar', 'v3', credentials=mod_gcal_session[session])
    
    request = service.events().patch(calendarId=calendarId, eventId=eventId, sendUpdates=notify , body=body_)
    response = request.execute()

    try:
        if result:
            SetVar(result, True)
    except Exception as e:
        if result:
            SetVar(result, False)
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "UpdateAtendeesEvent":
    emails = GetParams('emails')
    calendarId = GetParams('calendarId')
    eventId = GetParams('eventId')
    notify = GetParams("notify")
    result = GetParams('result')
    
    if emails.startswith("["):
        emails = eval(emails)
    else:
        emails = emails.split(",")
    
    if notify:
        notify = eval(notify)
        if notify:
            notify = "all"
    else:
        notify = "none"

    service = discovery.build('calendar', 'v3', credentials=mod_gcal_session[session])
    request = service.events().get(calendarId=calendarId, eventId=eventId)
    response = request.execute()
    
    emails_ = []
    for email in emails:
        emails_.append({'email': email.strip(), 'responseStatus': 'needsAction'})
    if 'attendees' in response:
        for email in response['attendees']:
            emails_.append(email)
    
    body_ = response
    body_["attendees"] = emails_    
    
    request2 = service.events().patch(calendarId=calendarId, eventId=eventId, sendUpdates=notify , body=body_)
    response2 = request2.execute()

    try:
        if result:
            SetVar(result, True)
    except Exception as e:
        if result:
            SetVar(result, False)
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e       

if module == "DeleteEvent":
    eventId = GetParams('eventId')
    calendarId = GetParams('calendarId')
    notify = GetParams("notify")
    result = GetParams('result')

    if notify:
        notify = eval(notify)
        if notify:
            notify = "all"
    else:
        notify = "none"

    service = discovery.build('calendar', 'v3', credentials=mod_gcal_session[session])

    request = service.events().delete(calendarId=calendarId, eventId=eventId, sendUpdates=notify)
    response = request.execute()

    try:
        if result:
            SetVar(result, True)
    except Exception as e:
        if result:
            SetVar(result, False)
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e