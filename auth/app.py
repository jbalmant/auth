#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask

from auth.api.domains import domains_blueprint
from auth.api.users import users_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('auth.settings.app.Configuration')

    app.register_blueprint(users_blueprint)
    app.register_blueprint(domains_blueprint)

    return app

