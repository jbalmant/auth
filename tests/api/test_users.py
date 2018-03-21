#!/usr/bin/env python
# -*- coding: utf-8 -*-
from auth.api import users


def test_users_must_true():
    assert users.return_true()
