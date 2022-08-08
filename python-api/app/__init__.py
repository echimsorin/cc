from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS
from app.extensions import mysql
from app.Dogs.controller import api as dogs_api
import os


def create_app():
    # Create a Flask application
    app = Flask(__name__)

    # Allow cross-origin resource sharing to let the front end access the backend
    CORS(app)

    # The flask_restx library helps us to create documentation at the /swagger-ui/ endpoint
    api = Api(app, title="Dogs API", version="0.1", doc="/swagger-ui/")

    # Connect your database
    if os.getenv("GAE_ENV", "").startswith("standard"):
        # For production in Google App Engine Standard
        app.config["MYSQL_DATABASE_HOST"] = os.environ["35.189.88.244"]
        app.config["MYSQL_DATABASE_PORT"] = 3306
        app.config["MYSQL_DATABASE_USER"] = os.environ["team-group-7"]
        app.config["MYSQL_DATABASE_PASSWORD"] = os.environ["CcF86q7iaeiWQwf2wy4B6KGUR"]
        app.config["MYSQL_DATABASE_DB"] = os.environ["bonds-group-7"]
    else:
        # For local execution
        app.config["MYSQL_DATABASE_HOST"] = "localhost"
        app.config["MYSQL_DATABASE_PORT"] = 3306
        app.config["MYSQL_DATABASE_USER"] = "root"
        app.config["MYSQL_DATABASE_PASSWORD"] = "Pa55w.rd"
        app.config["MYSQL_DATABASE_DB"] = "testdb"

    # Start the connector (found in extensions.py)
    mysql.init_app(app)

    # We add the Dogs module
    api.add_namespace(dogs_api, path="/dogs")

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
