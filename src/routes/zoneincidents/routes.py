from flask import current_app, json
from . import zoneIncidentsBP
import firebase_admin
from firebase_admin import db

@zoneIncidentsBP.route("/zoneincidents")
def getZoneIncidents():
    try:
        credentialObj = firebase_admin.credentials.Certificate(f'{current_app.root_path}/utils/certificate.json')
        defaultApp = firebase_admin.initialize_app(credentialObj, {
            'databaseURL': 'https://dbtt-1d7b5-default-rtdb.firebaseio.com/'
        })


        refReports = db.reference('reporte')
        zoneIncidents = refReports.get()
        return current_app.response_class(
            response=json.dumps({
                'ok': True,
                'message': 'success',
                'data': zoneIncidents
            }),
            mimetype='application/json'
        )
    except Exception as e:
        
        return current_app.response_class(
            status=500,
            response=json.dumps({'message': f'error {str(e)}', 'ok': False}),
            mimetype='application/json'
        )

@zoneIncidentsBP.route("/zoneincidents/<rangeRecords>")
def getZoneIncidentsRange(rangeRecords: str):
    try:
        credentialObj = firebase_admin.credentials.Certificate(f'{current_app.root_path}/utils/certificate.json')
        defaultApp = firebase_admin.initialize_app(credentialObj, {
            'databaseURL': 'https://dbtt-1d7b5-default-rtdb.firebaseio.com/'
        })
        
        limit = int(rangeRecords)

        refReports = db.reference('reporte')
        zoneIncidents = refReports.order_by_key().limit_to_first(limit).get()
        return current_app.response_class(
            response=json.dumps({
                'ok': True,
                'message': 'success',
                'data': zoneIncidents
            }),
            mimetype='application/json'
        )
    except Exception as e:
        
        return current_app.response_class(
            status=500,
            response=json.dumps({'message': f'error {str(e)}', 'ok': False}),
            mimetype='application/json'
        )
    