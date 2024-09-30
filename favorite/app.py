import os
from flask import Flask
from flask_migrate import Migrate
from routes import favorite_bp
from dotenv import load_dotenv
from models import db, init_app

load_dotenv()

file_path = os.path.abspath(os.getcwd()) + os.getenv('DATABASE_PATH')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(favorite_bp)
init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
