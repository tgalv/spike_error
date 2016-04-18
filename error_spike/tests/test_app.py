import unittest
import json

from error_spike import app


class TestErrorHandling(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_health(self):
        response = self.app.get('/')
        self.assertEquals(200, response.status_code)

    def test_5xx_error(self):
        response = self.app.get('/div_zero')
        self.assertEquals(500, response.status_code)

    def test_404_error(self):
        response = self.app.get('/foo')
        self.assertEquals(404, response.status_code)

    def test_good_json_post(self):
        response = self.app.post('/json_post',
                                 data=json.dumps({"name" : "Eggs", "price" : 34.99}), 
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'})
        self.assertEquals(200, response.status_code)

    def test_wrong_content_type(self):
        response = self.app.post('/json_post',
                                 data="<name>Eggs</name>", 
                                 headers={'Content-Type': 'text/xml',
                                          'Accept': 'application/json'})
        self.assertEquals(415, response.status_code)

    def test_accept_type(self):
        response = self.app.post('/json_post',
                                 data=json.dumps({"name" : "Eggs", "price" : 34.99}), 
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'text/xml'})
        self.assertEquals(406, response.status_code)

    def test_bad_schema(self):
        response = self.app.post('/json_post',
                                 data=json.dumps({"name" : 111, "price" : "222"}), 
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'})
        self.assertEquals(400, response.status_code)


if __name__ == "__main__":
    unittest.main()
