#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Configuration(object):
    DEBUG = True
    SERVICE_NAME = 'auth'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'

    ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    LOG_FILENAME = '/var/log/apps/{}'.format(SERVICE_NAME)

