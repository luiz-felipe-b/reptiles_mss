from flask import Blueprint, request, jsonify

from models import Reptile, db

reptile_bp = Blueprint('reptile', __name__, url_prefix='/reptile')

@reptile_bp.route('/all', methods=['GET'])
def get_all_reptiles():
    all_reptiles = Reptile.query.all()
    result = [reptile.serialize() for reptile in all_reptiles]
    response = {'message': 'Returning all reptiles', 'result': result}
    return jsonify(response), 200

@reptile_bp.route('/create', methods=['POST'])
def create_reptile():
    try:
        reptile = Reptile()
        reptile.name = request.form['name']
        reptile.slug = request.form['slug']
        reptile.species = request.form['species']
        reptile.genus = request.form['genus']
        reptile.size = request.form['size']
        reptile.weight = request.form['weight']
        reptile.image = request.form['image']

        db.session.add(reptile)
        db.session.commit()

        response = {'message': 'Reptile created', 'result': reptile.serialize()}
        code = 200
    except Exception as e:
        print(str(e))
        response = {'message': 'Reptile creation failed'}
        code = 400
    return jsonify(response), code

@reptile_bp.route('/<slug>', methods=['GET'])
def reptile_details(slug):
    reptile = Reptile.query.filter_by(slug=slug).first()
    if reptile:
        response = {'message': f'Returning details for {slug}', 'result': reptile.serialize()}
        code = 200
    else:
        response = {'message': f'Reptile {slug} not found'}
        code = 404
    return jsonify(response), code
