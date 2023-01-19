"""Flask app entry point"""

from flask import Flask


def create_app(config_name):
    """Flask app entry point"""
    app = Flask(__name__)
    config_module = f"web.config.{config_name.capitalize()}Config"
    app.config.from_object(config_module)

    @app.route("/")
    def hello():
        return "Hello World!"

    return app
