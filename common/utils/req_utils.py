import json 
 
import requests 
 
proxies = {"http": None, "https": None} 
 
_header = dict() 
_header["Content-Type"] = "application/json" 
 
 
def post_json(url, post_data, header=None): 
    if header is None: 
        header = dict() 
    header = dict(_header, **header) 
 
    response = requests.post(url, headers=header, data=json.dumps(post_data), timeout=30, proxies=proxies) 
    if response.status_code != 200: 
        return None 
    return response.text 
 
 
def get(url, para): 
    header = dict() 
    header["Content-Type"] = "application/json" 
 
    response = requests.get(url, para, headers=header, proxies=proxies, timeout=30) 
    if response.status_code != 200: 
        return None 
    return response.json() 
