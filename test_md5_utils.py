import unittest 
 
from common.utils.md5_utils import md5 
from common.utils.valid_utils import email_valid 
 
 
class Md5UtilsTest(unittest.TestCase): 
 
    # def tearDown(self): 
    #     print('tearDown') 
    # 
    # def setUp(self): 
    #     print("setUp") 
 
    def test_1(self): 
        ret = md5("ss@163.com") 
        assert ret == "026f86a21feda73b83d5eb2451b9945a" 
        self.assertEqual(ret, "026f86a21feda73b83d5eb2451b9945a") 
 
    def test_2(self): 
        ret = md5("ss@163.com", "111") 
        self.assertEqual(ret, "a2f84431111acc9c86059b25b0c1f5e9") 
 
    def test_email3(self): 
        ret = email_valid("@163") 
        self.assertFalse(ret) 
 
 
if __name__ == '__main__': 
    unittest.main() 




 
