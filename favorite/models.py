from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    reptile_id = db.Column(db.Integer, nullable=False)
    favorite = db.Column(db.Boolean, default=True)

    def __init__(self, user_id, reptile_id):
        self.user_id = user_id
        self.reptile_id = reptile_id

    def __repr__(self):
        return f'<Favorite {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'reptile_id': self.reptile_id,
            'favorite': self.favorite
        }
