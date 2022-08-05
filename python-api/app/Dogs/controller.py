from flask_restx import Namespace, Resource
from app import mysql


api = Namespace("dogs-controller", description="Api Controller for the dogs")  # noqa


@api.route("/")
class DogsResource(Resource):
    """Dogs Controller manages the api calls made to the /dogs/ endpoint."""

    def get(self):
        """Returns all dogs"""
        cursor = mysql.get_db().cursor()
        query = "SELECT * FROM dogs"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
