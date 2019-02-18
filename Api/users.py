from flask import Blueprint, request
from flask_restplus import Api, Resource

mod = Blueprint('users', __name__)
api = Api(mod)


# Use this endpoint(s) to modify a user object in the Database
@api.route('/user')
class User(Resource):
    def get(self):
        # TODO Query for this users information
        return "this gets a user"

    def post(self):
        user = request.get_json(force=True)
        # user should be a dict() of the json
        # TODO: ADD this user to the database
        print(user)
        return "this add/updates a user"

    def delete(self):
        # TODO: delete this user from the database
        return "this deletes a user"
