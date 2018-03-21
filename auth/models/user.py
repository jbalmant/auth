#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auth.app import db
from auth.models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def api_representation(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
