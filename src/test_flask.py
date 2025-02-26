import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_plus(self):
        response = self.client.get("/plus/4/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 7)

    def test_fac(self):
        response = self.client.get("/factorial/7")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 5040)
    
    def test_plus2(self):
        response = self.client.get("/plus/5/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 10)

    def test_ascii(self):
        response = self.client.get("/Ascii/A")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 65)
    
    
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

    def test_when_x_is_abba(self):
        response = self.client.get("palindrome/abba")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "True")
    
    def test_when_x_is_abc(self):
        response = self.client.get("samechar/abc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "True")

    def test_when_x_is_abbc(self):
        response = self.client.get("samechar/abbc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "False")

    def test_minus1(self):
        response = self.client.get("/minus/4/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 1)

    def test_when_x_is_2(self):
        response = self.client.get("/is_even/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "True")

    def test_when_x_is_3(self):
        response = self.client.get("/is_even/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "False")
    
    def test_is_odd_3(self):
        response = self.client.get("/is_odd/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "True")

    def test_is_odd_4(self):
        response = self.client.get("/is_odd/4")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "False")

    def test_is_odd_d(self):
        response = self.client.get("/is_odd/d")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Invalid number format')


    def test_multiple1(self):
        response = self.client.get("/multiple/4/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 12)

    def test_divide1(self):
        response = self.client.get("/divide/4/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], 2)

    def test_x_is_1(self):
        response = self.client.get("/cir_area/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], "3.14")

    def test_x_is_neg10(self):
        response = self.client.get("/cir_area/-10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], "0.00")

    def test_x_is_1dot5(self):
        response = self.client.get("/cir_area/1.5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['Result is'], "7.07")


if __name__ == "__main__":
    unittest.main()
    