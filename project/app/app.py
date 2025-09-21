from flask import Flask
from .routes import todo_bluePrint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bluePrint, url_prefix="/todos")
    return app