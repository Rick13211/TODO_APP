from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def createApp():
  app = Flask(__name__)
  db.__init__(app)
  app.config['SECRET_KEY'] = '123'
  app.config['SQLALCHMEY_DATABASE_URI'] = 'sqllite:///todo.db'
  from app.routes.auth import auth_bp
  from app.routes.auth import tasks_bp

  app.register_blueprint(auth_bp)
  app.register_blueprint(tasks_bp)
  
  return app