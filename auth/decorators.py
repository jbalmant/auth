#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from flask import request, current_app


def requires_json(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.mimetype not in ('application/json',):
            raise Exception('json supported')

        return f(*args, **kwargs)

    return decorated
