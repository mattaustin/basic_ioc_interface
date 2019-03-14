# -*- coding: utf-8 -*-
from dataclasses import dataclass

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
    user = users.get(username, None)
    if user and safe_str_cmp(
        user.password.encode("utf-8"), password.encode("utf-8")
    ):
        return user


def identify(payload):
    user_id = payload["identity"]
    return users.get(user_id, None)
