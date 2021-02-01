import json

from tests.BaseCase import BaseCase

class TestUserLogin(BaseCase):

    def test_successful_login(self):
        
        email = "awasthi.manas98@gmail.com"
        password = "testpassword"
        payload = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

    def test_login_with_invalid_email(self):
        email = "awasthi.manas98@gmail.com"
        password = "testpassword"
        payload = {
            "email": email,
            "password": password
        }
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        
        payload['email'] = "awasthi.manas98@gmail.com"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

       
        self.assertEqual("Invalid username or password", response.json['message'])        
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_password(self):
       
        email = "awasthi.manas98@gmail.com"
        password = "testpassword"
        payload = {
            "email": email,
            "password": password
        }
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

       
        payload['password'] = "testpassword"
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        
        self.assertEqual("Invalid username or password", response.json['message'])        
        self.assertEqual(401, response.status_code)