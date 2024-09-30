from flask import app
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from routes import bp
from dotenv import load_dotenv
import os

app = app.Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['WTF_CSRF_SECRET_KEY'] = os.getenv('WTF_CSRF_SECRET_KEY')
app.register_blueprint(bp)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'frontend.login'
login_manager.login_message = 'Please login.'

bootstrap = Bootstrap(app)

@login_manager.user_loader
def load_user(user_id):
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
