from flask import Blueprint
incidentBP = Blueprint('incidentBP', __name__)
from . import routes