# # -*- coding: utf-8 -*-
from caproto.sync import client
from flask import make_response, request
from flask_jwt_extended import jwt_required


@jwt_required
def put():
    response = make_response("")
    response.headers["Access-Control-Allow-Origin"] = "*"
    client.write(request.args.get("pv"), request.args.get("value"))
    return response
