# -*- coding: utf-8 -*-
from unittest import TestCase as BaseTestCase

from webput import app as webput


class ClientMixin:
    def setUp(self, *args, **kwargs):
        webput.app.config["TESTING"] = True
        self.client = webput.app.test_client()
        return super().setUp(*args, **kwargs)


class TestCase(ClientMixin, BaseTestCase):
    pass
