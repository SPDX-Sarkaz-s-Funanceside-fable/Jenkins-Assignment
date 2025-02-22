import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_plus(self):
        response = self.client.get("/plus/4/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 7)
    
    def test_when_x_is_17(self):
        response = self.client.get("/is_prime/17")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "True")
    
    def test_when_x_is_36(self):
        response = self.client.get("/is_prime/36")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "False")
    
    def test_when_x_is_2(self):
        response = self.client.get("/is_prime/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "True")
        
    def test_when_x_is_13219(self):
        response = self.client.get("is_prime/13219")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "True")

if __name__ == "__main__":
    unittest.main()
    