# -*- coding: utf-8 -*-
from unittest.mock import patch

from flask import make_response
from flask_jwt_extended import jwt_required

from webput.auth import User

from . import TestCase


class TestLogin(TestCase):
    def test_login_with_missing_json(self):
        response = self.client.post("/auth/login")

        self.assertEqual(response.status_code, 400)  # 400 Bas Request
        self.assertNotIn("access_token", response.json)

    def test_login_with_missing_credentials(self):
        response = self.client.post("/auth/login", json={})

        self.assertEqual(response.status_code, 401)  # 401 Not Authorised
        self.assertNotIn("access_token", response.json)

    @patch(
        "webput.auth.users",
        new={"username": User(username="username", password="password")},
    )
    def test_login_with_incorrect_username(self, *args):
        response = self.client.post(
            "/auth/login",
            json={"username": "incorrect-username", "password": "password"},
        )

        self.assertEqual(response.status_code, 401)  # 401 Not Authorised
        self.assertNotIn("access_token", response.json)

    @patch(
        "webput.auth.users",
        new={"username": User(username="username", password="password")},
    )
    def test_login_with_incorrect_password(self, *args):
        response = self.client.post(
            "/auth/login",
            json={"username": "username", "password": "incorrect-password"},
        )

        self.assertEqual(response.status_code, 401)  # 401 Not Authorised
        self.assertNotIn("access_token", response.json)

    @patch(
        "webput.auth.users",
        new={"username": User(username="username", password="password")},
    )
    def test_login_with_correct_credentials(self, *args):
        response = self.client.post(
            "/auth/login",
            json={"username": "username", "password": "password"},
        )

        self.assertEqual(response.status_code, 200)  # 200 OK
        self.assertIn("access_token", response.json)

    @patch(
        "webput.auth.users",
        new={"username": User(username="username", password="password")},
    )
    def test_protected_view_integration(self, *args):
        @jwt_required
        def view():
            return make_response("TEST")

        self.app.add_url_rule("/test", view_func=view, methods=["GET"])

        response = self.client.get("/test")

        self.assertEqual(response.status_code, 401)  # 401 Not Authorised
        self.assertNotIn(b"TEST", response.data)

        auth_response = self.client.post(
            "/auth/login",
            json={"username": "username", "password": "password"},
        )

        access_token = auth_response.json["access_token"]

        response = self.client.get(
            "/test", headers=[("Authorization", f"Bearer {access_token}")]
        )

        self.assertEqual(response.status_code, 200)  # 200 OK
        self.assertIn(b"TEST", response.data)
