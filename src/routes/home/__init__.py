from flask import Blueprint
homeBP = Blueprint('homeBP', __name__)
from . import routes
#Blueprint para tener rutas limpias y estrucuturadas
