from flask import current_app, json, jsonify
from . import homeBP
@homeBP.route("/")
def getAllEstado():
   return current_app.response_class(
      response=json.dumps({'message': 'hola', 'ok': True}),
      status=200,
      mimetype='application/json'
   )
