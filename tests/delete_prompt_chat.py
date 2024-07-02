import unittest  
import requests  
  
class TestChatPromptDeleteEndpoint(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/chat/prompt/_delete"  
  
    def test_delete_prompt_valid_request(self):   
        response = requests.delete(self.BASE_URL, params={'prompt_id': '12345'})  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt deleted successfully')  
  
    def test_delete_prompt_missing_parameters(self):  
        response = requests.delete(self.BASE_URL)  
        self.assertEqual(response.status_code, 400)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_delete_prompt_invalid_id(self):  
        response = requests.delete(self.BASE_URL, params={'prompt_id': 'invalid'})  
        self.assertEqual(response.status_code, 404)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_delete_prompt_invalid_method(self):   
        response = requests.post(self.BASE_URL)  
        self.assertEqual(response.status_code, 405)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_delete_prompt_unauthorized(self):  
        headers = {'Authorization': 'InvalidToken'}  
        response = requests.delete(self.BASE_URL, headers=headers, params={'prompt_id': '12345'})  
        self.assertEqual(response.status_code, 401)  
        self.assertIsNotNone(response.json().get('error'))  
  
if __name__ == '__main__':  
    unittest.main()  
