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
        password=User.generate_hash(data['password'])
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
    current_user = User.query.filter_by(username=data['username']).first()
    if not current_user:
        return json.dumps('{{message: User {} does not exist.}}'.format(data['username']))

    if User.verify_hash(data['password'], current_user.password):
        return json.dumps('{{message: Logged in as {}.}}'.format(current_user.username))

    return json.dumps('{message: Wrong credentials.}')
