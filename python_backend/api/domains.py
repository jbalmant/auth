#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import Blueprint

domains_blueprint = Blueprint('domains', __name__, url_prefix='/domains')


@domains_blueprint.route('/')
def get_domains():
    return json.dumps('{domains: ['
                      '{name: tivit, id=1},'
                      '{name: home, id=2},'
                      '{name: RJ, id=3},'
                      ']}'), 200
