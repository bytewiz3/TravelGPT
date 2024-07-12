import unittest  
import requests  
 
 
  
class TestUserRegister(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/user/_register"  
  
  
    def test_register_missing_username(self):  
        response = requests.post(self.BASE_URL, json={  
            "passwd": "testpassword",  
            "nickname": "testnick",  
            "phone": "1234567890",  
            "email": "testuser@example.com"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(400, response.json()["code"])  
        self.assertIn("field required", response.json()["msg"])  
      
    def test_register_invalid_password1(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "testuser",  
            "passwd": "testpassword",  
            "nickname": "testnick",  
            "phone": "1234567890",  
            "email": "testuser@example.com"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(420, response.json()["code"])  
        self.assertIn("密码必须包含大写字母", response.json()["msg"])   
      
    def test_register_invalid_password2(self):   
        response = requests.post(self.BASE_URL, json={  
            "username": "testuser",  
            "passwd": "Testpassword",  
            "nickname": "testnick",   
            "phone": "1234567890",  
            "email": "testuser@example.com"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(420, response.json()["code"])  
        self.assertIn("密码中至少包含一个数字", response.json()["msg"])  
  
    def test_register_invalid_password3(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "testuser",  
            "passwd": "Testpassword123",  
            "nickname": "testnick",  
            "phone": "1234567890",  
            "email": "testuser@example.com"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(420, response.json()["code"])  
        self.assertIn("密码中必须包含特殊字符", response.json()["msg"])  
      
    def test_register_success(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "testuser",  
            "passwd": "Testpassword123@",  
            "nickname": "testnick",  
            "phone": "1234567890",  
            "email": "testuser@example.com"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn("用户注册成功!", response.json()["msg"])  
  
    def test_register_duplicate_user(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "duplicateuser",  
            "passwd": "testpassword",  
            "nickname": "testnick",  
            "phone": "1234567890",  
            "email": "duplicateuser@example.com"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn("用户已经存在!", response.json()["msg"])  
  
if __name__ == "__main__":  
    unittest.main()   
 
 
 
  
