# Nombre proyecto: segurappAPI
# Estrcutura basica de una api con flask"Cambia el nombrede este titulo"
## Requisitos:
- Python 3.6.9
- LAMP para poder usar MySQL o XAMPP en windows
- Flask 1.1.2
- UBUNTU 18.04.5 LTS o windows 10
## Entorno en python
Antes de poder hacer tu proyecto tienes que crear tu entorno con python, comandos mas abajo.
## Variables de entorno:
Ubuntu:
- export FLASK_APP="app"
- export FLASK_ENV="development"
- export APP_SETTINGS_MODULE="config.local"
Windows
## Como usar este proyecto en UBUNTU 18.04.5 LTS
- Estar en la carpeta de api-sepomex
- Crear el entorno virtual desde la terminal: python3 -m venv venv, si manda un error ejecutar el siguiente comando en terminal: sudo apt install python3-venv
- Activar el entorno virtual, desde la terminal ejecutar el siguiente comando: . venv/bin/activate
- Instalar dependencias, en la terminal ejecutar lo siguiente: pip install -r requirements.txt
## Como usar en windows
- Estar en la carpeta de api-sepomex
- Crear el entorno virtual desde cmd: py -3 -m venv venv
- Activar el entorno virtal : .\venv\Scripts\activate.bat
- Instalar dependencias, en la terminal ejecutar lo siguiente: pip install -r requirements.txt
## Correr la app en local ya sea para ubuntu o windows
`flask run`
- set "APP_SETTINGS_MODULE=config.local"
- set "FLASK_APP=app"
- set "FLASK_ENV=development"
