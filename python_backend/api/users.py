#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Blueprint

users_blueprint = Blueprint('users', __name__, url_prefix='/users')


@users_blueprint.route('/')
def get_users():
    return json.dumps('{users: ['
                      '{name: Jonatas Balmant, id=1, age=30},'
                      '{name: Rocky Shimhity, id=2, age=24},'
                      '{name: Jesus Nazareno, id=3, age=32},'
                      '{name: Duponde, id=4, age=29},'
                      '{name: Bruninnha, id=3, age=32},'
                      ']}'), 200


def return_true():
    return True
