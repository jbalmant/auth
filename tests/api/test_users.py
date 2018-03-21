#!/usr/bin/env python
# -*- coding: utf-8 -*-
from python_backend.api import users


def test_users_must_true():
    assert users.return_true()
