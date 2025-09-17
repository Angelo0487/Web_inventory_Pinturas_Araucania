import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Base de datos compartida
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET', 'devkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'postgresql://admin:Angelo1989@host:55432/pinturas_araucania'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return app