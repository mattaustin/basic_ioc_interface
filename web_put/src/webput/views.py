# # -*- coding: utf-8 -*-
import time
import json

from caproto._utils import CaprotoTimeoutError
from caproto.sync import client
from flask import make_response, request
from flask_jwt_extended import jwt_required


@jwt_required
def get_channels_status():
    ''' process a list of pv names to get their metadata
    '''
    pvs = []
    chanNames = request.args.get('channels')
    if chanNames is not None:
        myNames = chanNames.split(',')
    else:
        return make_response("Error: no names")

    for name in myNames:
        pvInfo = {}
        pvInfo['name'] = name
        # get timestamp, severity
        try:
            val = client.read(name, data_type='time')
        except CaprotoTimeoutError:
            pvInfo['value'] = None
            pvInfo['timestamp'] = 0.0
            pvInfo['timestring'] = time.asctime(
                time.gmtime(pvInfo['timestamp'])
            )
        else:
            valValue = val.data.tolist()
            if val.data_count == 1:
                valValue = valValue[0]
            pvInfo['value'] = valValue
            pvInfo['timestamp'] = val.metadata.timestamp
            pvInfo['timestring'] = time.asctime(
                time.gmtime(pvInfo['timestamp'])
            )
            pvInfo['status'] = val.metadata.status
            pvInfo['severity'] = val.metadata.severity
        pvs.append(pvInfo)
    allValues = {'values': pvs}
    return make_response(json.dumps(allValues))


@jwt_required
def put():
    response = make_response("")
    response.headers["Access-Control-Allow-Origin"] = "*"
    client.write(request.args.get("pv"), request.args.get("value"))
    return response
