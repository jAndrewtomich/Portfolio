from datetime import datetime
from app import db


class Topic(db.Model):
    __tablename__ = 'topic'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    title = db.Column(db.String())
    content = db.Column(db.String())

    def __repr__(self):
        return f'<id> {self.id}'
 