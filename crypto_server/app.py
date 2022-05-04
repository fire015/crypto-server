from flask import Flask
from .http.controller import app as http_controller


def create_app():
    app = Flask(__name__)
    app.register_error_handler(Exception, handle_exception)
    app.register_blueprint(http_controller)

    return app


def handle_exception(e):
    return {"error": str(e)}, 500
