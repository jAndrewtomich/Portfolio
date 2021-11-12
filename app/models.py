from flask import current_app
from app import db


class Eda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    source = db.Column(db.String())
    height = db.Column(db.String())

    def __repr__(self):
        return "<Eda block #{}>".format(self.id)