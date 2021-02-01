from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from database.models import Movie
import json
from flask_restful import Api
from resources.routes import intitialize_routes
from resources.errors import errors

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '9b1a6c26db87b72cd8cee6814d39e1e7'

#app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb+srv://manas:hello12345@cluster0.16yoy.mongodb.net/moviedb?retryWrites=true&w=majority'
}

initialize_db(app)
intitialize_routes(api)

app.run()