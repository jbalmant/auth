#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Blueprint
from flask_restful import reqparse

from auth.models.user import User

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


@users_blueprint.route('/')
def get_users():
    users = User.query.filter_by().all()
    return json.dumps([u.api_representation() for u in users]), 200


@users_blueprint.route('/registration', methods=['POST'])
def registration():
    data = parser.parse_args()
    new_user = User(
        username=data['username'],
        password=data['password']
    )

    try:
        new_user.save_to_db()
        return json.dumps('{message:foi}'), 500
    except Exception as error:
        print(error.args[0])
        return json.dumps('{message:Something went wrong}'), 500


@users_blueprint.route('/login', methods=['POST'])
def login():
    data = parser.parse_args()
    return json.dumps('{logged}')
