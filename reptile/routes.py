from flask import Blueprint, request, jsonify

reptile_bp = Blueprint('reptile', __name__, url_prefix='/reptile')

@reptile_bp.route('/all', methods=['GET'])
def get_all_reptiles():
    return jsonify({'message': 'Returning all reptiles'}), 200

@reptile_bp.route('/create', methods=['POST'])
def create_reptile():
    return jsonify({'message': 'Creating a reptile'}), 201

@reptile_bp.route('/<slug>', methods=['GET'])
def reptile_details(slug):
    return jsonify({'message': f'Returning details for {slug}'}), 200
