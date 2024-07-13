import unittest  
import requests  
 
 
   
class TestChatPromptUpdateEndpoint(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/chat/prompt/_update"  
 
      
    def test_update_prompt_valid_request(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "Updated prompt text"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
    def test_update_prompt_valid_request(self):  
        payload = {  
            "prompt_id": "1235",  
            "new_prompt": "another Updated prompt text"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
    def test_update_prompt_valid_request(self):  
        payload = {  
            "prompt_id": "1345",  
            "new_prompt": "Updated prompt text2"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
          
  
    def test_update_prompt_missing_fields(self):  
        payload = {  
            "prompt_id": "12345"  
            # Missing new_prompt field  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Missing required fields', response.json().get('error'))  
   
    def test_update_prompt_sql_injection(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "Updated prompt'; DROP TABLE prompts;--"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
    def test_update_prompt_html_content(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "<div>Updated prompt</div>"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
    def test_update_prompt_sql_injection(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "Updated prompt'; DROP TABLE prompts;--"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
    def test_update_prompt_json_content(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": '{"text": "Updated prompt"}'  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
  
    def test_update_prompt_invalid_data(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": 12345  # Invalid data type for new_prompt  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Invalid data format', response.json().get('error'))  
  
    def test_update_prompt_invalid_method(self):  
        response = requests.get(self.BASE_URL)  
        self.assertEqual(response.status_code, 405)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_update_prompt_long_new_prompt(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "a" * 1001  # Assuming max length is 1000  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('New prompt exceeds maximum length', response.json().get('error'))  
  
    def test_update_prompt_special_characters(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "!@#$%^&*()_+"  
        }   
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
   
    def test_update_prompt_unauthorized(self):  
        headers = {'Authorization': 'InvalidToken'}  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "Updated prompt text"  
        }  
        response = requests.put(self.BASE_URL, headers=headers, json=payload)  
        self.assertEqual(response.status_code, 401)  
        self.assertIsNotNone(response.json().get('error'))  
  
if __name__ == '__main__':  
    unittest.main()  
 
 
 
  
