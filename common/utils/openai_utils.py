import json 
import os 
 
import array 
import httpx 
from dotenv import load_dotenv 
from openai import OpenAI 
from apps.base.log import logger 
 
from common.utils import load_yaml, load_json 
 
load_dotenv() 
 
# Load application configuration 
cfg = load_yaml("config/application.yaml") 
 
pre_messages = load_json("config/pre_message.json") 
 
# Timeout for API requests 
timeout = os.environ.get("OPENAI_API_TIMEOUT") or cfg.get("open_ai").get("timeout") 
# API_KEY 
api_key = os.environ.get("OPENAI_API_KEY") or cfg.get("open_ai").get("api_key") 
# System content 
sys_content = os.environ.get("OPENAI_API_SYS_CONTENT") or cfg.get("open_ai").get("sys_content") 
# Travel content 
travel_content = os.environ.get("OPENAI_API_TRAVEL_CONTENT") or cfg.get("open_ai").get("travel_content") 
# Model to use 
model = os.environ.get("OPENAI_API_MODEL") or cfg.get("open_ai").get("model") 
# Proxy settings 
proxy = os.environ.get("OPENAI_API_PROXY") or cfg.get("open_ai").get("proxy") or None 
# HTTP client with proxy if specified 
http_client = httpx.Client(proxy=proxy) if proxy else httpx.Client() 
 
client = OpenAI( 
    timeout=timeout, 
    api_key=api_key, 
    http_client=http_client, 
) 
 
 
async def get_openai_stream_generator(request_messages: array): 
    message_list = [] 
    message_list.extend(pre_messages) 
    message_list.extend(request_messages) 
 
    new_message_list = [item for item in message_list if 
                        item.get('role') == 'user' or item.get('role') == 'system' or item.get('role') == 'assistant'] 
 
    stream = client.chat.completions.create( 
        model=model or "gpt-4", 
        messages=new_message_list, 
        stream=True, 
    ) 
 
    for event in stream: 
        logger.info(event) 
        # if await request1.is_disconnected(): 
        #     print("Connection disconnected") 
        #     break 
        answer = event.choices[0].delta.content 
        yield json.dumps({'message': '', 'code': 0, 'data': answer}, ensure_ascii=False) 
 
 
async def get_openai_generator(request_messages: array): 
    message_list = [] 
    message_list.extend(pre_messages) 
    message_list.extend(request_messages) 
 
    chat_completion = client.chat.completions.create( 
        model=model or "gpt-4", 
        messages=message_list 
    ) 
    print(chat_completion.choices[0].message.content) 
 
 
async def get_pre_messages(): 
    return pre_messages 
