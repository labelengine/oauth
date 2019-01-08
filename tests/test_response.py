import unittest
from app.response import error_message, json_response

from app import app

class TestResponse(unittest.TestCase):
    def setUp(self):
        app.test_client

    def test_error_message(self):
        with app.test_request_context():
            error_message("Test error")

    def test_json_response(self):
        with app.test_request_context():
            json_response({"message": "test response"})
