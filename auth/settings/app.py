#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Configuration(object):
    SQLALCHEMY_DATABASE_URI = ''
    SERVICE_NAME = 'python_backend'

    ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    LOG_FILENAME = '/var/log/apps/{}'.format(SERVICE_NAME)