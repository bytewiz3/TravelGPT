import requests 
import json 
import hmac 
import hashlib 
import base64 
import urllib.parse 
import time 
 
 
class DingDingUtils: 
 
  def __init__(self, secret, webhook): 
    self.secret = secret 
    self.webhook = webhook 
 
  def sign(self): 
    timestamp = str(round(time.time() * 1000)) 
    string_to_sign = '{}\n{}'.format(timestamp, self.secret) 
    string_to_sign_enc = string_to_sign.encode('utf-8') 
    hmac_code = hmac.new(self.secret.encode('utf-8'), string_to_sign_enc, digestmod=hashlib.sha256).digest() 
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code)) 
    sign_str = {"sign": sign, "timestamp": timestamp} 
    return sign_str 
 
  def send_msg(self, title, message): 
    data = { 
      "msgtype": "markdown", 
      "markdown": { 
        "title": title, 
        "text": message 
      }, 
      # @Group Members 
      # "at": { 
      #     "atMobiles": [ 
      #         "150XXXXXXXX" 
      #     ], 
      #     "atUserIds ": [ 
      #         "user123" 
      #     ], 
      #     "isAtAll": false 
      # } 
    } 
    sign = self.sign() 
    url = self.webhook + '&timestamp=' + sign['timestamp'] + '&sign=' + sign['sign'] 
    headers = {"Content-Type": "application/json"} 
    print(url) 
    r = requests.post(url, data=json.dumps(data), headers=headers) 
    print(r.text) 
 
 
if __name__ == '__main__': 
  p_secret = 'SEC835c6d134cd89948ef0c0b08f79b16c5878c39c979d75c37db439e27fc41c11a' 
  p_webhook = "https://oapi.dingtalk.com/robot/send?access_token=75965177288e3937992227281130be3299c142227cc7ca0ba87d03481fb1fd0c" 
  ding_ding_utils = DingDingUtils(p_secret, p_webhook) 
  ding_ding_utils.send_msg("title", "message") 
