import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Base de datos compartida
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración general
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET', 'devkey')

    # ⚡ Usa SQLite por defecto (archivo local inventario.db)
    # Si existe DATABASE_URL en las variables de entorno → se usará (ej: PostgreSQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'sqlite:///inventario.db'
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return app
