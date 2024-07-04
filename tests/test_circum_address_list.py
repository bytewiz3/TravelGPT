import unittest  
import requests  
  
class TestUserRegister(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/address/circum_address_list"  
  
    def test_address_no_params(self):  
        response = requests.post(self.BASE_URL, json={})  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(420, response.json()["code"])  
        self.assertIn("", response.json()["msg"])  
      
    def test_address_empty_vals(self):  
        response = requests.post(self.BASE_URL, json={  
            "address_name": ""  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(420, response.json()["code"])  
        self.assertIn("", response.json()["msg"])  
      
    def test_circum_address_sucess1(self):  
        response = requests.post(self.BASE_URL, json={  
            "address_name": "杭州西湖"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn("900", response.json()["msg"]["count"])  
        self.assertIn("10000", response.json()["msg"]["infocode"])  
      
    def test_circum_address_sucess2(self):  
        response = requests.post(self.BASE_URL, json={  
            "address_name": "成都武侯祠"  
        }) 
        self.assertEqual(response.status_code, 200)  
        self.assertIn("900", response.json()["msg"]["count"])  
        self.assertIn("10000", response.json()["msg"]["infocode"])  
