from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Movie(db.Document):
    popularity = db.FloatField(required=True)
    director = db.StringField(required=True)
    name = db.StringField(required=True, unique=True)
    genre = db.ListField(db.StringField(), required=True)
    imdb_score = db.FloatField(required = True)

class User(db.Document):
    email = db.EmailField(required = True, unique = True)
    password = db.StringField(required = True, min_length = 6)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
 