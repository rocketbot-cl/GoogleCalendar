



# Google Calendar
  
You can get, modify, create or delete events and more from any calendar you have in your Google Calendar account  

*Read this in other languages: [English](Manual_GoogleCalendar.md), [Português](Manual_GoogleCalendar.pr.md), [Español](Manual_GoogleCalendar.es.md)*
  
![banner](imgs/Modulo_GoogleCalendar.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

Before using this module, you must register your app into Google Cloud Portal.

1. Sign in with a google account and get into the following link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete the form to create a new proyect and then press "Create".
3. Within the Navigation Menu (Left), get into API and Services.
4. Go to the upper section and press "+ ENABLE API AND SERVICES".
5. Search for "Google Calendar API", select it and then press "ENABLE".
6. Go back to the Navigation Menu, go to API and Services and then get into Credentials.
7. Press Create Credentials and select OAuth Client ID. Then select Application Type: Desktop App, give it a name and press Create.
8. Download the credentials JSON file.
9. Finally, go back to the Navigation Menu, go to Consent Screen and add your user in the "Test Users" section (even if it is the same that is creating the app).

Note: When the first connection is made, a .pickle 
file will be created in the Rocketbot root folder, to connect to the same service with another account you must give each session a name. If credentials expire you must delete the .pickle file and create and download a new credentials (JSON) file.


## Description of the commands

### Setup G-Suite credentials
  
Get permissions to handle Google SpreadSheet with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path|JSON file with the credentials to access the Google Calentar API.|C:/path/to/credentials.json|
|Port (Optional)||8080|
|Session||session|

### List Calendars
  
List user calendars
|Parameters|Description|example|
| --- | --- | --- |
|Result||Variable|
|Session||session|

### List Events
  
List events of a user's calendar
|Parameters|Description|example|
| --- | --- | --- |
|ID de calendario||Calendar ID|
|Result||Variable|
|Session||session|

### Get Event
  
Get an event from a calendar
|Parameters|Description|example|
| --- | --- | --- |
|ID de calendario||Calendar ID|
|ID de evento||Event ID|
|Result||Variable|
|Session||session|

### Create Event
  
Create an event within a user's calendar
|Parameters|Description|example|
| --- | --- | --- |
|Event Data||{'summary': 'Google I/O 2015', 'location': '800 Howard St., San Francisco, CA 94103', 'description': 'A chance to hear more about Google's developer products.', 'start': {'dateTime': '2015-05-28T09:00:00-07:00', 'timeZone': 'America/Los_Angeles'}, 'end': {'dateTime': '2015-05-28T17:00:00-07:00', 'timeZone': 'America/Los_Angeles'}, 'recurrence': ['RRULE:FREQ=DAILY;COUNT=2'], 'attendees': [{'email': 'lpage@example.com'}, {'email': 'sbrin@example.com'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 1440}, {'method': 'popup', 'minutes': 10}]}}}|
|ID de calendario||Calendar ID|
|Title ||New Event|
|Location ||800 Howard St., San Francisco, CA 94103|
|Description ||Event for...|
|Start Date ||2015-05-28T09:00:00|
|Start Timezone ||America/Los_Angeles|
|End Date ||2015-05-28T12:00:00|
|End Timezone ||America/Los_Angeles|
|Recurrence |For building the recurrence rule visit the documentation https//developers.google.com/calendar/api/v3/reference/events/insert|['RRULE:FREQ=DAILY;COUNT=2']|
|Attendees |For more than one attendee build a list of dictionaries, for only one attendee build a dictionary.|[{'email': 'lpage@example.com'}, {'email': 'sbrin@example.com'}]|
|Reminders |For more than one reminder build a list of dictionaries, for only one build a dictionary.|[{'method': 'email', 'minutes': 1440}, {'method': 'popup', 'minutes': 10}]|
|Send notifications|Send notifications by email|-|
|Result||Variable|
|Session||session|

### Update Event
  
Update an event within a user's calendar
|Parameters|Description|example|
| --- | --- | --- |
|Data to Modify||{'attendees': [{'email': 'lpage@example.com'}, {'email': 'sbrin@example.com'}]}|
|ID de calendario||Calendar ID|
|ID de evento||Event ID|
|Send notifications|Send notifications by email|-|
|Result||Variable|
|Session||session|

### Update Assistants
  
Update attendees to an event
|Parameters|Description|example|
| --- | --- | --- |
|Data to Modify||['lpage@example.com', 'sbrin@example.com']|
|ID de calendario||Calendar ID|
|ID de evento||Event ID|
|Send notifications|Send notifications by email|-|
|Result||Variable|
|Session||session|

### Delete Event
  
Delete an event from a user's calendar
|Parameters|Description|example|
| --- | --- | --- |
|ID de evento||Event ID|
|ID de calendario||Calendar ID|
|Send notifications|Send notifications by email|-|
|Result||Variable|
|Session||session|
