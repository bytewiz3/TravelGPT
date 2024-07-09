import unittest  
import requests  
 
  
class TestSaveChatHistory(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/chat/_save"  
  
    def test_save_chat_history_success(self):  
        # Define a sample payload for a successful request  
        payload = {  
            "user_id": "user123",  
            "chat_id": "chat456",  
            "history": [  
                {"timestamp": "2023-01-01T12:00:00Z", "message": "Hello!"},  
                {"timestamp": "2023-01-01T12:01:00Z", "message": "How are you?"}  
            ]  
        }  
 
         
        # Make the POST request  
        response = requests.post(self.BASE_URL, json=payload)  
  
        # Assert the response status code and message  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Chat history saved successfully')  
  
    def test_save_chat_history_missing_fields(self):  
        # Define a payload with missing required fields  
        payload = {  
            "user_id": "user123",  
            # Missing chat_id and history  
        }  
  
        # Make the POST request  
        response = requests.post(self.BASE_URL, json=payload)  
  
        # Assert the response status code and error message  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Missing required fields', response.json().get('error'))  
  
    def test_save_chat_history_invalid_data(self):  
        # Define a payload with invalid data   
        payload = {  
            "user_id": "user123",  
            "chat_id": "chat456",  
            "history": "This should be a list, not a string"  
        }  
  
        # Make the POST request  
        response = requests.post(self.BASE_URL, json=payload)  
  
        # Assert the response status code and error message  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Invalid data format', response.json().get('error'))  
  
if __name__ == '__main__':  
    unittest.main()  
 
 
