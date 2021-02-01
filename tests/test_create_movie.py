import json

from tests.BaseCase import BaseCase

class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        email = "awasthi.manas98@gmail.com"
        password = "testpassword"
        user_payload = json.dumps({
            "email": email,
            "password": password
        })

        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
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
        # When
        response = self.app.post('/api/movies',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(movie_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)