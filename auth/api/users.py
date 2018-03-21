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
    return json.dumps('{users: ['
                      '{name: Jonatas Balmant, id=1, age=30},'
                      '{name: Rocky Shimhity, id=2, age=24},'
                      '{name: Jesus Nazareno, id=3, age=32},'
                      '{name: Duponde, id=4, age=29},'
                      '{name: Bruninnha, id=3, age=32},'
                      ']}'), 200


@users_blueprint.route('/registration', methods=['POST'])
def registration():
    data = parser.parse_args()
    new_user = User(
        username=data['username'],
        password=data['password']
    )

    try:
        new_user.save_to_db()
        return {
            'message': 'User {} was created.'.format(data['username'])
        }
    except:
        return {'message': 'Something went wrong'}, 500


@users_blueprint.route('/login', methods=['POST'])
def login():
    data = parser.parse_args()
    return json.dumps('{logged}')
