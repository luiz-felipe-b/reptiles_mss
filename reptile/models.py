from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)

class Reptile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    species = db.Column(db.String(100), unique=True, nullable=False)
    genus = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    image = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Reptile {self.id} {self.name}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'species': self.species,
            'genus': self.genus,
            'size': self.size,
            'weight': self.weight,
            'image': self.image
        }
