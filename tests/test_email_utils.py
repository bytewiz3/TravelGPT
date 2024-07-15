import unittest 
 
from common.utils.email_utils import send_email 
 
 
class EmailUtilsTest(unittest.TestCase): 
 
    def tearDown(self): 
        print('tearDown') 
 
    def setUp(self): 
        print("setUp") 
 
    def test_send_email(self): 
        ret = send_email("test标题", "test内容", ["89428467@qq.com"]) 
        self.assertTrue(ret) 
 
 
if __name__ == '__main__': 
    unittest.main() 




