import unittest 
 
from common.utils.valid_utils import email_valid 
 
 
class EmailUtilsTest(unittest.TestCase): 
 
    # def tearDown(self): 
    #     print('tearDown') 
    # 
    # def setUp(self): 
    #     print("setUp") 
 
    def test_email1(self): 
        ret = email_valid("ss@163.com") 
        self.assertTrue(ret) 
 
    def test_email2(self): 
        ret = email_valid("@163.com") 
        self.assertFalse(ret) 
 
    def test_email3(self): 
        ret = email_valid("@163") 
        self.assertFalse(ret) 
 
 
if __name__ == '__main__': 
    unittest.main() 

