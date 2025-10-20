from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createApp():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = '123'
    # Corrected the key and value
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    db.init_app(app)
    # Corrected the import statements
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    return app