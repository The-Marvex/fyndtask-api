from flask import Response, request, session
from database.models import Movie
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, MovieAlreadyExistsError, InternalServerError, MovieNotExistsError

class MoviesApi(Resource):

    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            movie = Movie(**body).save()
            id = movie.id
            return{'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class MovieApi(Resource):

    @jwt_required
    def put(self, id):
        try:
            body = request.get_json()
            Movie.objects.get(id=id).update(**body)
            return 'Successfully Updated', 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception as e:
            raise InternalServerError



    @jwt_required
    def delete(self, id):
        try:
            Movie.objects.get(id=id).delete()
            return 'Successfully Deleted', 200
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception as e:
            raise InternalServerError
        
    def get(self, id):
        movie = Movie.objects.get(id=id).to_json()
        return Response(movie, mimetype="application/json", status=200)

class delMovie(Resource):

    @jwt_required
    def delete(self):
        try:
            name = request.args.get('name')
            Movie.objects.get(name=name).delete()
            return 'Successfully Deleted', 200
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception as e:
            raise InternalServerError

class search(Resource):

    def get(self):
        try:
            name = request.args.get('name')
            movie = Movie.objects.get(name=name).to_json()
            return Response(movie, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception as e:
            raise InternalServerError

class update(Resource):

    @jwt_required
    def put(self):
        try:
            name = request.args.get("name")
            body = request.get_json()
            Movie.objects.get(name=name).update(**body)
            return 'Successfully Updated', 200
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception as e:
            raise InternalServerError 




