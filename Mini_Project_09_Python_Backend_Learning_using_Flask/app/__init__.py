from flask import Flask
# Import the Flask class from the flask module to create the web application.

app = Flask(__name__)
# Create an instance of the Flask class, which represents the Flask application.
# `__name__` allows Flask to determine the root path of the application for loading resources.

from app import routes
# Import the `routes` module (or file) from the `app` package.
# This ensures that the route handlers are registered with the application.