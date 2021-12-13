#entry point: rutas
import os
from flask import Flask
from src import create_app
settingsModule = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settingsModule)
