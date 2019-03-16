# -*- coding: utf-8 -*-
from unittest import TestCase as BaseTestCase

import webput


class ClientMixin:
    def setUp(self, *args, **kwargs):
        self.app = webput.create_app(test_config={"TESTING": True})
        self.client = self.app.test_client()
        return super().setUp(*args, **kwargs)


class TestCase(ClientMixin, BaseTestCase):
    pass
