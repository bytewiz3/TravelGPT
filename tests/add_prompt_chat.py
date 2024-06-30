import unittest  
import requests  
   
class TestChatPromptAddEndpoint(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/chat/prompt/_add"  
  
    def test_add_prompt_valid_request(self):  
        payload = {  
            "user_id": "user123",  
            "prompt": "Hello, how can I assist you today?"  
        }  
        response = requests.post(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt added successfully')  
  
    def test_add_prompt_valid_request(self):  
        payload = {  
            "user_id": "user123",  
            "prompt": "Hello, what's your traval dates?"  
        }  
        response = requests.post(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt added successfully')  
  
  
    def test_add_prompt_valid_request(self):  
        payload = {  
            "user_id": "user123",  
            "prompt": "Thanks for more information, here's a new travel plan generated for you"  
        }  
        response = requests.post(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt added successfully')  
  
    def test_add_prompt_missing_fields(self):  
        payload = {  
            "user_id": "user123"  
            # Missing prompt field  
        }  
        response = requests.post(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Missing required fields', response.json().get('error'))  
  
    def test_add_prompt_invalid_data(self):  
        payload = {  
            "user_id": "user123",  
            "prompt": 12345  # Invalid data type for prompt  
        }  
        response = requests.post(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Invalid data format', response.json().get('error'))  
  
    def test_add_prompt_invalid_method(self):  
        response = requests.get(self.BASE_URL)  
        self.assertEqual(response.status_code, 405)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_add_prompt_unauthorized(self):  
        headers = {'Authorization': 'InvalidToken'}  
        payload = {   
            "user_id": "user123",  
            "prompt": "Hello, how can I assist you today?"  
        }  
        response = requests.post(self.BASE_URL, headers=headers, json=payload)  
        self.assertEqual(response.status_code, 401)  
        self.assertIsNotNone(response.json().get('error'))  
  
if __name__ == '__main__':  
    unittest.main()  
