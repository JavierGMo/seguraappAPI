from flask import current_app, json, request
import requests

from src.consts.firebase import URL_DB_FIREBASE

from . import userBP

@userBP.route("/users")
def getUsers():
    try:
        requestFireBase = requests.get(
            f'{URL_DB_FIREBASE}usuario.json'
        )
        data = requestFireBase.json()

        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'data': data,
                'ok': True
            }),
            status=200,
            mimetype='application/json'
        )
    except:
        return current_app.response_class(
            response=json.dumps({
                'message': 'error',
                'ok': False
            }),
            status=500,
            mimetype='application/json'
        )

@userBP.route("/users/<userid>")
def getUser(userid: str):
    try:
        requestFireBase = requests.get(
            f'{URL_DB_FIREBASE}usuario/{userid}.json'
        )
        if requestFireBase.status_code != 200:
            return current_app.response_class(
                response=json.dumps({
                    'message': 'error',
                    'ok': False
                }),
                status=requestFireBase.status_code,
                mimetype='application/json'
            )
        data = requestFireBase.json()
        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'data': data,
                'ok': True
            }),
            mimetype='application/json'
        )
    except:
        return current_app.response_class(
            response=json.dumps({
                'message': 'error',
                'ok': False
            }),
            status=500,
            mimetype='application/json'
        )
@userBP.route("/users", methods=['POST'])
def createUser():
    try:
        nombre = request.json['nombre']
        apellidos = request.json['apellidos']
        edad = request.json['edad']
        fechadecreacion = request.json['fechadecreacion']
        lugarprocedencia = request.json['lugarprocedencia']

        requestFireBase = requests.post(
            f'{URL_DB_FIREBASE}usuario.json',
            json={
                'nombre': nombre,
                'apellidos': apellidos,
                'edad': edad,
                'fechadecreacion': fechadecreacion,
                'lugarprocedencia': lugarprocedencia
            }
        )
        data = requestFireBase.json()
        if requestFireBase.status_code != 200:
            return current_app.response_class(
                response=json.dumps({
                    'message': 'error',
                    'data': data,
                    'ok': False
                }),
                status=requestFireBase.status_code,
                mimetype='application/json'
            )
        
        

        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'data': data,
                'ok': True
            }),
            status=requestFireBase.status_code,
            mimetype='application/json'
        )
    except:
        return current_app.response_class(
            response=json.dumps({
                'message': 'error interno',
                'ok': False
            }),
            status=500,
            mimetype='application/json'
        )