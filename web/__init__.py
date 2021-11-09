from flask import Flask

from web.auth_route import auth


def create_app():
    app = Flask(__name__, )
    app.config.from_mapping(
    )
    app.register_blueprint(auth)

    return app