from flask import current_app, json, request

from src.consts.firebase import URL_DB_FIREBASE
from . import reportBP

import requests

@reportBP.route("/report")
def getReports():
    response = None
    try:
        requestDBFireBase = requests.get(
            f'{URL_DB_FIREBASE}reporte.json',
        )
        if requestDBFireBase.status_code != 200:
            return current_app.response_class(
                response=json.dumps({'message': 'error', 'ok': False}),
                status=requestDBFireBase.status_code,
                mimetype='application/json'
            )
        data = requestDBFireBase.json()
        
        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'ok': True,
                'data': data
            }),
            status=200,
            mimetype='application/json'
        )
    except:
        return current_app.response_class(
            response=json.dumps({'message': 'error', 'ok': False}),
            status=500,
            mimetype='application/json'
        )

@reportBP.route("/report/<idreport>")
def getReport(idreport: str):
    
    try:
        requestDBFireBase = requests.get(
            f'{URL_DB_FIREBASE}reporte/{idreport}.json',
        )
        if requestDBFireBase.status_code != 200:
            return current_app.response_class(
                response=json.dumps({'message': 'error', 'ok': False}),
                status=requestDBFireBase.status_code,
                mimetype='application/json'
            )
        data = requestDBFireBase.json()
        
        return current_app.response_class(
            response=json.dumps({
                'message': 'success',
                'ok': True,
                'data': data
            }),
            status=200,
            mimetype='application/json'
        )
    except:
        return current_app.response_class(
            response=json.dumps({'message': 'error', 'ok': False}),
            status=500,
            mimetype='application/json'
        )

@reportBP.route("/report", methods=["POST"])
def createReports():
    
    try:
        print(request.json['datetime'])
        dateTime = request.json['datetime'].split('|')
        dateReport = dateTime[0]
        timeReport = dateTime[1]
        refUser = request.json['refUser']
        refVideo = 'https://www.cloudinary.com/ref/asd1DAS1WDAS12as'
        zonaIncidente = 1
        requestDBFireBase = requests.post(
            f'{URL_DB_FIREBASE}reporte.json',
            json={
                "fechaincidente": dateReport,
                "horaincidente": timeReport,
                "refUsuario": refUser,
                "refvideo": refVideo,
                "zonaincidente": zonaIncidente
            }
        )
        
        if requestDBFireBase.status_code  == 200:
            data = requestDBFireBase.json()
            
            return current_app.response_class(
                response=json.dumps({
                    'message': 'success',
                    'ok': True,
                    'data': data
                }),
                status=200,
                mimetype='application/json'
            )
        else:
            return current_app.response_class(
            response=json.dumps({
                'message': 'error',
                'ok': False,
                'data': requestDBFireBase.json()
            }),
            status=requestDBFireBase.status_code,
            mimetype='application/json'
        )
    except NameError:
        print(NameError)
        return current_app.response_class(
            response=json.dumps({'message': 'error', 'ok': False}),
            status=500,
            mimetype='application/json'
        )