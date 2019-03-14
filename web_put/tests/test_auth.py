# -*- coding: utf-8 -*-
from . import TestCase


class TestAuth(TestCase):
    def test_auth_with_invalid_credentials(self):
        r = self.client.post("/auth")
        raise NotImplementedError(r)
