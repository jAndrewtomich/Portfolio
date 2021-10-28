from flask import current_app
from app import db


class Eda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_block = db.Column(db.String(), nullable=False)
    iframes = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return "<Eda block #{}>".format(self.id)

