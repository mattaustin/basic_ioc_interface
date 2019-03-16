# -*- coding: utf-8 -*-

__title__ = "webput"

__version__ = "0.0+dev1"

__url__ = "https://github.com/webepics/basic_ioc_interface"


def create_app(test_config=None):
    import os

    from flask import Flask
    from flask_jwt_extended import JWTManager

    from . import auth, views

    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = os.environ.get("WEBPUT_SECRET_KEY")

    if test_config:
        app.config.update(test_config)

    jwt = JWTManager(app)
    jwt.user_loader_callback_loader(auth.user_loader_callback)

    app.add_url_rule("/auth/login", view_func=auth.login, methods=["POST"])
    app.add_url_rule(
        "/get", view_func=views.get_channels_status, methods=["GET"]
    )
    app.add_url_rule("/put", view_func=views.put, methods=["POST"])

    return app


if __name__ == "__main__":
    create_app().run()
