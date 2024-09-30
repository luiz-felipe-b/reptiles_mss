import os
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify, make_response
import requests
from models import Favorite, db

load_dotenv()

favorite_bp = Blueprint('favorite', __name__, url_prefix='/favorite')

user_api_url = os.getenv('USER_API_URL')

def get_user(api_key):
    headers = {
        'Authorization': api_key
    }
    response = requests.get(user_api_url, headers=headers)
    if response.status_code != 200:
        return {'message': 'Not authorized'}, 404
    user = response.json()
    return user

@favorite_bp.route('/all', methods=['GET'])
def get_favorites():
    api_key = request.headers.get('Authorization')
    if not api_key:
        return jsonify({'message': 'Not logged in'}), 401
    response = get_user(api_key)
    user = response.get('result')
    if not user:
        return jsonify({'message': 'Not logged in'}), 401
    favorites = Favorite.query.filter_by(user_id=user['id'], favorite=True).all()
    if not favorites:
        return jsonify({'message': 'No favorites found'}), 404
    return jsonify({'message': 'Returning all favorites', 'result': [favorite.serialize() for favorite in favorites]}), 200

@favorite_bp.route('/toggle', methods=['POST'])
def favorite_toggle():
    try:
        api_key = request.headers.get('Authorization')
        if not api_key:
            return jsonify({'message': 'Not logged in'}), 401
        response = get_user(api_key)
        if not response.get('result'):
            return jsonify({'message': 'Not logged in'}), 401
        user = response.get('result')
        reptile_id = int(request.form['reptile_id'])
        user_id = user['id']
        target = Favorite.query.filter_by(user_id=user_id, reptile_id=reptile_id).first()
        if target is None:
            favorite = Favorite(user_id=user_id, reptile_id=reptile_id)
            db.session.add(favorite)
            db.session.commit()
            return jsonify({'message': 'Favorite added', 'result': favorite.serialize()}), 200
        else:
            target.favorite = not target.favorite
            db.session.commit()
            return jsonify({'message': 'Favorite toggled', 'result': target.serialize()}), 200
    except Exception as e:
        return jsonify({'message': 'Favorite toggling failed'}), 400
