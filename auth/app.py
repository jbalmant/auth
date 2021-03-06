#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('auth.settings.app.Configuration')

    db.init_app(app)

    jwt = JWTManager(app)

    from auth.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    if app.debug:
        print('Running in debug mode')
    else:
        print('NOT running in debug mode')

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app

