import random 
import string 
 
 
def random_str(s_len=10): 
    return ''.join(random.sample(string.ascii_letters + string.digits + '!@#$%^&*()_+=-', s_len)) 
 
 
print(random_str(50)) 
