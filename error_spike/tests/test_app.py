import unittest

from error_spike import app

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/helloworld/')
        self.assertEquals(200, response.status_code)
