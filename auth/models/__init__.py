#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auth.app import db
from datetime import datetime


class BaseModel (db.Model):
    __abstract__ = True

    created_dt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_dt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

from auth.models.user import User
