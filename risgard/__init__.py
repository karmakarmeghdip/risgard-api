from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Keep this global
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    
    with app.app_context():
        from . import firebase
        from . import routes

        db.create_all()

        return app