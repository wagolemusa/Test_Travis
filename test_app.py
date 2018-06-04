from app import app
import unittest
import json


BASE_URL = 'http://127.0.0.1:5000/api/v1/users/requests'
BAD_ITEM_URL = '{}/5'.format(BASE_URL)
GOOD_ITEM_URL = '{}/3'.format(BASE_URL)

class TestFlaskApi(unittest.TestCase):




    def test_user_request(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.1:5000/api/v1/users/requests')
        self.assertEqual(response.status_code, 200)
        

        
    def test_get_user_id(self):
        tester = app.test_client(self)
        response = tester.get('http://127.0.0.1:5000/api/v1/users/requests/<int:user_id>')
        self.assertEqual(response.status_code, 404)
        


    def test_create_request(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/users/requests',data=json.dumps(
            dict(name="kevin", username="wise", email="me@gmail.com")),
            content_type="application/json")
        self.assertEqual(response.status_code, 301)
    

    def test_update_user(self):
        tester = app.test_client(self)
        response = tester.put('/api/v1/users/requests/<int:user_id>',data=json.dumps(
            dict(name="kevin", username="wise", email="me@gmail.com")),
            content_type="application/json")
        self.assertEqual(response.status_code, 404)


    

if __name__ == "__main__":
    unittest.main()