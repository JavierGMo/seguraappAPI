from flask import current_app, json, request
from src.consts.firebase import URL_DB_FIREBASE
from . import incidentBP

import requests

@incidentBP.route('/incidentes')
def getIncidentes():
    try:
        requestDBFireBase = requests.get(f'{URL_DB_FIREBASE}incidentes.json')
        if requestDBFireBase.status_code != 200:
            return current_app.response_class(
                response=json.dumps({
                    'message': 'error',
                    'ok': False
                }),
                status=requestDBFireBase.status_code,
                mimetype='application/json'
            )
        
        data = requestDBFireBase.json()
        
        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'data':data,
                'ok': True
            }),
            status=requestDBFireBase.status_code,
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

@incidentBP.route('/incidentes/<idincident>')
def getIncidente(idincident: str):
    try:
        requestDBFireBase = requests.get(f'{URL_DB_FIREBASE}incidentes/{idincident}.json')
        if requestDBFireBase.status_code != 200:
            return current_app.response_class(
                response=json.dumps({
                    'message': 'error',
                    'ok': False
                }),
                status=requestDBFireBase.status_code,
                mimetype='application/json'
            )
        
        data = requestDBFireBase.json()
        
        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'data':data,
                'ok': True
            }),
            status=requestDBFireBase.status_code,
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

@incidentBP.route('/incidentes', methods=["POST"])
def createIncidente():
    try:
        titulo = request.json['titulo']
        descripcion = request.json['descripcion']
        tipo = request.json['tipo']
        body = {
            "titlo": titulo,
            "descripcion": descripcion,
            "tipo": tipo
        }
        requestDBFireBase = requests.post(
            f'{URL_DB_FIREBASE}incidentes.json',
            json=body
        )
        if requestDBFireBase.status_code != 200:
            return current_app.response_class(
                response=json.dumps({
                    'message': 'error',
                    'ok': False
                }),
                status=requestDBFireBase.status_code,
                mimetype='application/json'
            )
        
        data = requestDBFireBase.json()
        
        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'data':data,
                'ok': True
            }),
            status=requestDBFireBase.status_code,
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