



# Google Calendar
  
Puedes obtener, modificar, crear o borrar eventos y más de cualquier calendario que tengas en tu cuenta de Google Calendar  

*Read this in other languages: [English](Manual_GoogleCalendar.md), [Português](Manual_GoogleCalendar.pr.md), [Español](Manual_GoogleCalendar.es.md)*
  
![banner](imgs/Modulo_GoogleCalendar.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  
## Como usar este modulo

Antes de usar este módulo, debe registrar su aplicación en Google Cloud Portal.

1. Inicie sesión con una cuenta de Google y acceda al siguiente enlace: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete el formulario para crear un nuevo proyecto y luego presione "Crear".
3. Dentro del menú de navegación (izquierda), acceda a API y servicios.
4. Ve a la sección superior y presiona "+ HABILITAR API Y SERVICIOS".
5. Busque "Google Calendar API", selecciónelo y luego presione "HABILITAR".
6. Vuelva al menú de navegación, vaya a API y servicios y luego acceda a Credenciales.
7. Pulse Crear credenciales y seleccione ID de cliente de OAuth. Luego seleccione Tipo de aplicación: Aplicación de escritorio, asígnele un nombre y presione Crear.
8. Descargue el archivo JSON de credenciales.
9. Finalmente, vuelve al Menú de Navegación, ve a la Pantalla de Consentimiento y agrega tu usuario en la sección "Usuarios de prueba" (aunque 
sea el mismo que está creando la aplicación).

Nota: Cuando se realiza la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio con otra cuenta, debe asignar un nombre a cada sesión. Si las credenciales caducan, debe eliminar el archivo .pickle y crear y descargar un archivo de credenciales nuevo (JSON).

## Descripción de los comandos

### Configurar credenciales G-Suite
  
Obtiene los permisos para manejar Google SpreadSheet con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo de credenciales|Archivo JSON con las credenciales de acceso a la API de Google Calentar.|C:/ruta/a/credenciales.json|
|Puerto (Opcional)||8080|
|Session||session|

### Listar calendarios
  
Listar los calendarios de un usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Resultado||Variable|
|Session||session|

### Listar Eventos
  
Listar eventos de un calendario del usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Calendar ID||Calendar ID|
|Resultado||Variable|
|Session||session|

### Obtener Evento
  
Obtener un evento de un calendario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Calendar ID||Calendar ID|
|Event ID||Event ID|
|Resultado||Variable|
|Session||session|

### Crear Evento
  
Crear un evento dentro del calendario de un usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Datos de Evento||{'summary': 'Google I/O 2015', 'location': '800 Howard St., San Francisco, CA 94103', 'description': 'A chance to hear more about Google's developer products.', 'start': {'dateTime': '2015-05-28T09:00:00-07:00', 'timeZone': 'America/Los_Angeles'}, 'end': {'dateTime': '2015-05-28T17:00:00-07:00', 'timeZone': 'America/Los_Angeles'}, 'recurrence': ['RRULE:FREQ=DAILY;COUNT=2'], 'attendees': [{'email': 'lpage@example.com'}, {'email': 'sbrin@example.com'}], 'reminders': {'useDefault': False, 'overrides': [{'method': 'email', 'minutes': 1440}, {'method': 'popup', 'minutes': 10}]}}}|
|Calendar ID||Calendar ID|
|Titulo ||Nuevo Evento|
|Ubicación ||800 Howard St., San Francisco, CA 94103|
|Descipción ||Evento para...|
|Fecha de Inicio ||2015-05-28T09:00:00|
|Zona Horaria de Inicio ||America/Los_Angeles|
|Fecha de Fin ||2015-05-28T12:00:00|
|Zona horaria de fin ||America/Los_Angeles|
|Frecuencia |Para armar la regla de frecuencia visite la documentación https//developers.google.com/calendar/api/v3/reference/events/insert|['RRULE:FREQ=DAILY;COUNT=2']|
|Invitados |Para más de un invitado armar una lista de diccionarios, para solo un invitado armar un diccionario.|[{'email': 'lpage@example.com'}, {'email': 'sbrin@example.com'}]|
|Recordatorios |Para más de un recordatorio armar una lista de diccionarios, para solo uno armar un diccionario.|[{'method': 'email', 'minutes': 1440}, {'method': 'popup', 'minutes': 10}]|
|Enviar notificaciones|Enviar notificaciones por correo electronico|-|
|Resultado||Variable|
|Session||session|

### Actualizar Evento
  
Actualizar un evento dentro del calendario de un usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Datos a Modificar||{'attendees': [{'email': 'lpage@example.com'}, {'email': 'sbrin@example.com'}]}|
|Calendar ID||Calendar ID|
|Event ID||Event ID|
|Enviar notificaciones|Enviar notificaciones por correo electronico|-|
|Resultado||Variable|
|Session||session|

### Actualizar Asistentes
  
Actualizar asistentes a un evento
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Datos a Modificar||['lpage@example.com', 'sbrin@example.com']|
|Calendar ID||Calendar ID|
|Event ID||Event ID|
|Enviar notificaciones|Enviar notificaciones por correo electronico|-|
|Resultado||Variable|
|Session||session|

### Borrar Evento
  
Borrar un evento del calendario de un usuario
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Event ID||Event ID|
|Calendar ID||Calendar ID|
|Enviar notificaciones|Enviar notificaciones por correo electronico|-|
|Resultado||Variable|
|Session||session|
