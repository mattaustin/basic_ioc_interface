# -*- coding: utf-8 -*-
from dataclasses import dataclass

from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp


@dataclass
class User:

    username: str

    password: str


user_list = [
    User(username="user", password="password"),
    User(username="user2", password="password2"),
]


users = {user.username: user for user in user_list}


def authenticate(username, password):
    user = users.get(username)
    if user and safe_str_cmp(
        user.password.encode("utf-8"), password.encode("utf-8")
    ):
        return user


def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    user = authenticate(
        username=request.json.get("username"),
        password=request.json.get("password"),
    )

    if not user:
        return jsonify({"message": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.username)

    return jsonify(access_token=access_token), 200


def user_loader_callback(identity):
    return users.get(identity)
