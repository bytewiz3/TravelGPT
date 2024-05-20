# -*- coding: utf-8 -*-
import array
import json
import os

import httpx
from openai import OpenAI

from apps.api.base import error, success, check_not_empty
from apps.api.chat_pri import save_chat_history
from apps.api.service.history_service import get_history_by_session_id
from apps.api.user.user import CurrentUser
from apps.base.log import logger
from fastapi import APIRouter, Depends
from dotenv import load_dotenv
from sse_starlette.sse import EventSourceResponse

from common.utils import load_yaml
from common.utils.id_worker import DefaultIdWorker
from common.utils.openai_utils import get_openai_stream_generator, get_openai_generator, get_pre_messages

route = APIRouter()

load_dotenv()

# Read application configuration
cfg = load_yaml("config/application.yaml")

# Request timeout
timeout = os.environ.get("OPENAI_API_TIMEOUT") or cfg.get("open_ai").get("timeout")
# API_KEY
api_key = os.environ.get("OPENAI_API_KEY") or cfg.get("open_ai").get("api_key")
# System content
sys_content = os.environ.get("OPENAI_API_SYS_CONTENT") or cfg.get("open_ai").get("sys_content")
# Session start content
travel_content = os.environ.get("OPENAI_API_TRAVEL_CONTENT") or cfg.get("open_ai").get("travel_content")
# Model in use
model = os.environ.get("OPENAI_API_MODEL") or cfg.get("open_ai").get("model")
# Proxy
proxy = os.environ.get("OPENAI_API_PROXY") or cfg.get("open_ai").get("proxy") or None
# HTTP client with proxy
http_client = httpx.Client(proxy=proxy) if proxy else httpx.Client()

client = OpenAI(
    timeout=timeout,
    api_key=api_key,
    http_client=http_client,
)

travel_message = [{"role": "travel", "content": travel_content}]

@logger.catch()
@route.post("/_new_chat", summary='Create a new chat session')
async def new_chat():
    user = CurrentUser(None, None)
    session_id = "N" + str(DefaultIdWorker.get_id())
    new_message = {"session_id": session_id, "messages": travel_message}
    await save_chat_history(user, new_message)
    return success("Successfully created a new temporary session", new_message)


@logger.catch()
@route.post("/_chat", summary='Send messages to ChatGPT')
async def chat(message: dict):
    """
     {"session_id", "123", "role":"user", "content":"Hello"}
    """
    session_id = message.get("session_id")
    content = message.get("content")
    check_not_empty(session_id, "Session ID cannot be empty")
    check_not_empty(content, "Message content cannot be empty")

    your_message = {"role": "user", "content": content}
    logger.info(f"Sending message: `{your_message}`")

    # Get message history
    history_message_list = await get_history_by_session_id(session_id)
    message_list = []
    for item in history_message_list:
        message_list.append(item.get("message"))
    message_list.append(your_message)

    # Save your message
    await save_chat_history(None, {
        "session_id": session_id,
        "messages": [your_message]
    })

    # Send message, return a streaming response
    return EventSourceResponse(get_openai_stream_generator(message_list))


@logger.catch()
@route.post("/_save", summary='Save message history')
async def save(message: dict = None):
    """
     {"session_id", "123", "role":"user","content":"Hello"}
    """
    session_id = message.get("session_id")
    content = message.get("content")
    check_not_empty(session_id, "Session ID cannot be empty")
    check_not_empty(content, "Message content cannot be empty")

    await save_chat_history(None, {
        "session_id": session_id,
        "messages": [{"role": message.get("role"), "content": content}]
    })
    return success("Session saved successfully", {"session_id": session_id})


