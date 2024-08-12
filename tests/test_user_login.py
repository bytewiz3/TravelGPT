import unittest  
import requests  
 
  
class TestUserRegister(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/user/_login"  
 
     
    def test_user_login_success(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "testuser",  
            "passwd": "Testpassword123@"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn("Login successful!", response.json()["msg"])  
        self.assertIn("1793420037466497024", response.json()["data"]["user_id"])  
        self.assertIn("testuser", response.json()["testuser"]["username"])  
        self.assertIn("testnick", response.json()["testnick"]["nickname"])  
 
     
    def test_user_login_invalid_password(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "testuser",  
            "passwd": "Testpassword123"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn("登录失败! 用户不存在或密码不正确!", response.json()["msg"])  
      
    def test_user_login_invalid_username(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "nottestuser",  
            "passwd": "Testpassword123@"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn("登录失败! 用户不存在或密码不正确!", response.json()["msg"])  
      
    def test_user_login_missing_username(self):  
        response = requests.post(self.BASE_URL, json={  
            "passwd": "Testpassword123@"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(400, response.json()["code"])  
        self.assertIn("field required", response.json()["msg"])  
      
    def test_user_login_missing_password(self):  
        response = requests.post(self.BASE_URL, json={  
            "username": "testuser"  
        })  
        self.assertEqual(response.status_code, 200)  
        self.assertIn(400, response.json()["code"])  
        self.assertIn("field required", response.json()["msg"])  
 
 
 
