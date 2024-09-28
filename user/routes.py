from flask import Blueprint, jsonify, make_response, request
from flask_login import current_user, login_user, logout_user
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/all', methods=['GET'])
def get_all_users():
    all_user = User.query.all()
    result = [user.serialize() for user in all_user]
    response = {
        'message': 'Returning all users',
        'result': result
    }
    return jsonify(response), 200

@user_bp.route('/create', methods=['POST'])
def create_user():
    try:
        user = User()
        user.username = request.form["username"]
        user.password = generate_password_hash(request.form["password"], method='pbkdf2:sha256')
        user.is_admin = True

        db.session.add(user)
        db.session.commit()
        response = {
            'message': 'Success',
            'result': user.serialize()
        }
        code = 201
    except Exception as e:
        print(str(e))
        response = {
            'message': 'Error in creating response',
        }
        code = 409
    return jsonify(response), code

@user_bp.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if not user:
        code = 401
        return jsonify({'message': 'Invalid username or password'}), code
    if check_password_hash(user.password, password):
        user.update_api_key()
        db.session.commit()
        login_user(user)
        response = {
            'message': 'Logged in',
            'api_key': user.api_key,
            'result': user.serialize()
        }
        code = 200
        return make_response(jsonify(response), code)
    response = { 'message': 'Access denied'}
    return make_response(jsonify(response), code)

@user_bp.route('/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'Logged out'}), 200
    return jsonify({'message': 'Not logged in'}), 401

@user_bp.route('/<username>/exists', methods=['GET'])
def user_exists(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User exists'}), 200
    return jsonify({'message': 'User does not exist'}), 404

@user_bp.route('/', methods=['GET'])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify({'result':current_user.serialize()}), 200
    return jsonify({'message': 'Not logged in'}), 401
