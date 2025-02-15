import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_plus(self):
        response = self.client.get("/plus/4/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 7)

if __name__ == "__main__":
    unittest.main()
    