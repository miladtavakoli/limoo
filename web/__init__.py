from flask import Flask, jsonify

from utils.exceptions import CustomException
from web.auth_route import auth


def create_app():
    app = Flask(__name__, )
    app.config.from_mapping(
    )
    app.register_blueprint(auth)

    return app


app = create_app()


