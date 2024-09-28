import os
from flask import Flask
from routes import reptile_bp
from dotenv import load_dotenv

load_dotenv()

file_path = os.path.abspath(os.getcwd()) + os.getenv('DATABASE_PATH')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path + os.getenv('DATABASE_PATH')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(reptile_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
