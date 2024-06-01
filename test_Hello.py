import unittest
from app import app
class TesHelloWorld(unittest.TestCase):

  def setup(self):
    self.client = app.test_client()
  def test_hello_world(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Hello, World', respone.data)
