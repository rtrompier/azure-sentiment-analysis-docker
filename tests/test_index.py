import unittest

from src.index import app

class TestSentimentAnalysis(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_response(self):
        response = self.app.get('/?sentence=I really be happy to work at hugging face')
        body = response.get_json()
        self.assertTrue(isinstance(body, list))
        self.assertEqual(body[0]['label'], '5 stars')
        self.assertIsNotNone(body[0]['score'])

    def test_error_response(self):
        response = self.app.get('/')
        self.assertTrue(response.get_json()['error'], 'Pass a sentence as query parameter for a personalized response.')