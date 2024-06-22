import os 
 
import redis as redis 
from dotenv import load_dotenv 
 
from common.utils import load_yaml 
 
load_dotenv() 
 
# Load application configuration  
cfg = load_yaml("config/application.yaml") 
 
# redis host 
redis_host = os.environ.get("REDIS_HOST") or cfg.get("redis").get("host") 
# redis port 
redis_port = os.environ.get("REDIS_PORT") or cfg.get("redis").get("port") 
# redis db 
redis_db = os.environ.get("REDIS_DB") or cfg.get("redis").get("db") 
 
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db) 
 
 
class RedisUtils: 
 
    @staticmethod 
    def set(k, v): 
        redis_client.set(k, v) 
 
    @staticmethod 
    def get(k): 
        return redis_client.get(k) 
 
    @staticmethod 
    def delete(k): 
        redis_client.delete(k) 
 
    @staticmethod 
    def set_ex(k, v, expire): 
        redis_client.setex(k, expire, v) 
