import unittest  
import requests  
 
 
class TestChatHistoryEndpoint(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/chat/history/list"  
 
     
    def test_retrieve_chat_history_valid_request(self):  
        response = requests.get(self.BASE_URL, params={'userId': '12345'})  
        self.assertEqual(response.status_code, 200)  
        self.assertGreater(len(response.json()), 0)  
        self.assertIsNotNone(response.json())  
  
    def test_retrieve_chat_history_missing_parameters(self):  
        response = requests.get(self.BASE_URL)  
        self.assertEqual(response.status_code, 400)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_retrieve_chat_history_invalid_user_id(self):  
        response = requests.get(self.BASE_URL, params={'userId': 'invalid'})  
        self.assertEqual(response.status_code, 404)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_retrieve_chat_history_no_history(self):  
        response = requests.get(self.BASE_URL, params={'userId': '67890'})  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(len(response.json()), 0)  
  
    def test_retrieve_chat_history_invalid_method(self):  
        response = requests.post(self.BASE_URL)  
        self.assertEqual(response.status_code, 405)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_retrieve_chat_history_unauthorized(self):  
        headers = {'Authorization': 'InvalidToken'}  
        response = requests.get(self.BASE_URL, headers=headers)  
        self.assertEqual(response.status_code, 401)  
        self.assertIsNotNone(response.json().get('error'))  
  
if __name__ == '__main__':  
    unittest.main()  
 
 
 
