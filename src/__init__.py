import os 
from flask import Flask
from flask_cors import CORS, cross_origin
def create_app(settingsModule):
   app = Flask(__name__, instance_relative_config=True)
   #Config app
   print("settings module: {}".format(settingsModule))
   app.config.from_object(settingsModule)
   # Cors
   cors = CORS(app)
   app.config['CORS_HEADERS'] = 'Content-Type'
   #Aqui deben ir los Blueprints para las rutas que crees.
   #Los Blueprints son para las rutas en este caso.
   #Se recomienda buscar mas sobre estos
   #Blueprints para las rutas
   #Solo esta la ruta de home
   from .routes.home import homeBP
   from .routes.report import reportBP
   from .routes.user import userBP

   app.register_blueprint(homeBP)
   app.register_blueprint(reportBP)
   app.register_blueprint(userBP)

   return app
