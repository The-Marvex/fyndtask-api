import unittest
import json

from tests.BaseCase import BaseCase

class TestGetMovies(BaseCase):

    def test_empty_response(self):
        response = self.app.get('/api/movies')
        self.assertListEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    def test_movie_response(self):
        
        email = "awasthi.manas98@gmail.com"
        password = "testpassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
        user_id = response.json['id']
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['token']

        movie_payload = {
            "popularity": 88.0,
            "director": "Michael Curtiz",
            "genre": [
                "Drama",
                "Romance",
                " War"
            ],
            "imdb_score": 8.8,
            "name": "Casablanca"
        }
        response = self.app.post('/api/movies',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(movie_payload))

        
        response = self.app.get('/api/movies')
        added_movie = response.json[0]

        
        self.assertEqual(movie_payload['name'], added_movie['name'])
        self.assertEqual(movie_payload['genre'], added_movie['genre'])
        self.assertEqual(movie_payload['director'], added_movie['director'])
        self.assertEqual(movie_payload['imdb_score'], added_movie['imdb_score'])
        self.assertEqual(movie_payload['popularity'], added_movie['popularity'])
        self.assertEqual(200, response.status_code)