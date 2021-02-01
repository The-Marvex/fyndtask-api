from .movie import MovieApi, MoviesApi, delMovie, search, update
from .auth import SignupApi, LoginApi

def intitialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')
    api.add_resource(delMovie, '/api/delete')
    api.add_resource(search, '/api/search')
    api.add_resource(update, '/api/update')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    
