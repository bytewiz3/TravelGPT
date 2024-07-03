import unittest  
import requests  
  
class TestChatPromptListEndpoint(unittest.TestCase):  
    BASE_URL = "http://localhost:8089/api/v1/chat/prompt/list"  
   
    def test_get_prompt_list_valid_request(self):  
        response = requests.get(self.BASE_URL)  
        self.assertEqual(response.status_code, 200)  
        self.assertGreater(len(response.json()), 0)  
        self.assertIsNotNone(response.json())  
  
    def test_get_prompt_list_invalid_method(self):  
        response = requests.post(self.BASE_URL)  
        self.assertEqual(response.status_code, 405)  
        self.assertIsNotNone(response.json().get('error'))  
    def test_update_prompt_unauthorized(self):  
        headers = {'Authorization': 'InvalidToken'}  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "Updated prompt text"  
        }  
        response = requests.put(self.BASE_URL, headers=headers, json=payload)  
        self.assertEqual(response.status_code, 401)  
        self.assertIsNotNone(response.json().get('error'))  
  
    def test_update_prompt_nonexistent_id(self):  
        payload = {  
            "prompt_id": "nonexistent",  
            "new_prompt": "Updated prompt text"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 404)  
        self.assertEqual(response.json().get('error'), 'Prompt not found')  
  
    def test_update_prompt_internal_server_error(self):  
        payload = {  
            "prompt_id": "error",  
            "new_prompt": "Updated prompt text"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 500)  
        self.assertEqual(response.json().get('error'), 'Internal Server Error')  
  
    # New test cases with varied payloads  
    def test_update_prompt_empty_new_prompt(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": ""  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Invalid new prompt', response.json().get('error'))  
  
    def test_update_prompt_null_new_prompt(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": None  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Invalid new prompt', response.json().get('error'))  
  
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
  
    def test_update_prompt_javascript_content(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "<script>alert('Hello');</script>"  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
    def test_update_prompt_whitespace_content(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "    "  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 400)  
        self.assertIn('Invalid new prompt', response.json().get('error'))  
  
    def test_update_prompt_minimum_length_prompt(self):  
        payload = {  
            "prompt_id": "12345",  
            "new_prompt": "a"  # Assuming min length is 1  
        }  
        response = requests.put(self.BASE_URL, json=payload)  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json().get('message'), 'Prompt updated successfully')  
  
    def test_get_prompt_list_unauthorized(self):  
        headers = {'Authorization': 'InvalidToken'}  
        response = requests.get(self.BASE_URL, headers=headers)  
        self.assertEqual(response.status_code, 401)  
        self.assertIsNotNone(response.json().get('error'))  
  
if __name__ == '__main__':  
    unittest.main()  
