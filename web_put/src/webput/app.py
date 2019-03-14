# -*- coding: utf-8 -*-
from caproto.sync import client
from flask import Flask, make_response, request
from flask_jwt import JWT, jwt_required, current_identity

from . import auth


app = Flask(__name__)


jwt = JWT(
    app=app,
    authentication_handler=auth.authenticate,
    identity_handler=auth.identify,
)


@app.route("/put", methods=["POST"])
@jwt_required()
def put():
    response = make_response("")
    response.headers["Access-Control-Allow-Origin"] = "*"
    client.write(request.args.get("pv"), request.args.get("value"))
    return response
