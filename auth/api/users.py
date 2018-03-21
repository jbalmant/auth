#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Blueprint
from flask_restful import reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

from auth.models.user import User

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


@users_blueprint.route('/')
@jwt_required
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
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])
        return json.dumps('{{'
                          'message: User {} was created.'.format(data['username']),
                          'access_token: {}'.format(access_token),
                          'refresh_token: {}'.format(refresh_token),
                          '}}')
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
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])

        return json.dumps('{{message: Logged in as {}., access_token: {},  refresh_token: {}}}'
                          .format(data['username'], access_token, refresh_token))

    return json.dumps('{message: Wrong credentials.}')


@users_blueprint.route('/secret')
@jwt_required
def secret():
    response = {'message': 'anwser is 42'}
    return json.dumps(response)
