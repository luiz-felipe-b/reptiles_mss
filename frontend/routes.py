from flask import Blueprint, flash, render_template, request, session, redirect, url_for
from flask_login import current_user

from api.reptile_client import ReptileClient
from api.favorite_client import FavoriteClient
import forms
from api.user_api import UserClient

bp = Blueprint('frontend', __name__)

@bp.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        session['favorite'] = FavoriteClient.get_favorites()
    try:
        reptiles = ReptileClient.get_reptiles()
    except:
        reptiles = {'result': []}
    return render_template('index.html', reptiles=reptiles.get('result'))

@bp.route('/register', methods=['POST', 'GET'])
def register():
    form = forms.RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            if UserClient.user_exists(username):
                flash('User already exists.')
                return render_template('register.html', form=form)
            else:
                user = UserClient.create_user(form)
                if user:
                    flash("Registered. Please login.")
                    return redirect(url_for('frontend.index'))
        else:
            flash('Invalid form.')
    return render_template('register.html', form=form)

@bp.route('/login', methods=['POST', 'GET'])
def login():
    form = forms.LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            api_key = UserClient.login(form)
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']
                flash('Logged in.')
                return redirect(url_for('frontend.index'))
            else:
                flash('Invalid credentials.')
        else:
            flash('Invalid form.')
    return render_template('login.html', form=form)

@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('Logged out.')
    return redirect(url_for('frontend.index'))

@bp.route('/reptile/<slug>', methods=['GET', 'POST'])
def reptile_detailes(slug):
    response = ReptileClient.get_reptile(slug)
    reptile = response.get('result')
    favorites = FavoriteClient.get_favorites().get('result')

    form = forms.FavoriteForm(request.form)
    favorite = favorite_check(reptile.get('id'), favorites)

    if request.method == 'POST':
        if 'user' not in session:
            flash('Please login')
            return redirect(url_for('frontend.login'))
        FavoriteClient.toggle_favorites(reptile_id=reptile.get('id'))
        if not favorite:
            flash(f'{reptile.get("name")} removed from favorites.')
        else:
            flash(f'{reptile.get('name')} added to favorites.')
    return render_template('reptile_info.html', reptile=reptile, favorites=favorites, form=form, favorite_check=favorite_check)

def favorite_check(reptile_id, favorites):
    return any(favorite['reptile_id'] == reptile_id for favorite in favorites)
