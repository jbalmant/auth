#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auth.app import db
from auth.models import BaseModel
from passlib.hash import pbkdf2_sha256 as sha256


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

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
