"""Web Server Gateway Interface"""
import os

from web.app import create_app

app = create_app(os.environ["FLASK_CONFIG"])
