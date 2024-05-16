# -*- coding: utf-8 -*-
import json
import os

import httpx
from openai import OpenAI
from sqlalchemy import asc, and_, or_, update

from apps.api.base import error, success, check_not_empty, check_not_empty_list
from apps.api.service.history_service import get_history_by_session_id
from apps.api.user.user import CurrentUser
from apps.base.db import new_session
from apps.base.log import logger
from fastapi import APIRouter, Depends
from dotenv import load_dotenv
from sse_starlette.sse import EventSourceResponse

from apps.models import ChatHistory, Relation
from common.utils import load_yaml
from common.utils.id_worker import DefaultIdWorker
from itertools import groupby
from operator import itemgetter

from common.utils.openai_utils import get_openai_stream_generator, get_openai_generator

route = APIRouter()


load_dotenv()

# Read application configuration
cfg = load_yaml("config/application.yaml")

# Access timeout
timeout = os.environ.get("OPENAI_API_TIMEOUT") or cfg.get("open_ai").get("timeout")
# API_KEY
api_key = os.environ.get("OPENAI_API_KEY") or cfg.get("open_ai").get("api_key")
# System content
sys_content = os.environ.get("OPENAI_API_SYS_CONTENT") or cfg.get("open_ai").get("sys_content")
# Travel content
travel_content = os.environ.get("OPENAI_API_TRAVEL_CONTENT") or cfg.get("open_ai").get("travel_content")
# Model in use
model = os.environ.get("OPENAI_API_MODEL") or cfg.get("open_ai").get("model")
# Proxy
proxy = os.environ.get("OPENAI_API_PROXY") or cfg.get("open_ai").get("proxy") or None
# Client with proxy
http_client = httpx.Client(proxy=proxy) if proxy else httpx.Client()

client = OpenAI(
    # base_url="https://api.openai-proxy.com/",
    timeout=timeout,
    api_key=api_key,
    http_client=http_client,
)

travel_message = [{"role": "travel", "content": travel_content}]


# @logger.catch()
# @route.post("/_new_chat_pri", summary='Create a new session')
# async def new_chat_pri(user: CurrentUser = Depends(CurrentUser)):
#     travel_message = {
#         "messages": [{"role": "travel", "content": travel_content}]
#     }
#     session_id = await save_chat_history(user, travel_message)
#     travel_message.update({"session_id": session_id})
#
#     message_list = [{
#         "role": "user",
#         "content": sys_content or "Now you are a travel expert, master of travel time planning."
#     }]
#     await get_openai_generator(message_list)
#
#     return success("New session created successfully", travel_message)

@logger.catch()
@route.post("/_new_chat_pri", summary='Create a new session')
async def new_chat_pri(user: CurrentUser = Depends(CurrentUser)):
    session_id = "U" + str(DefaultIdWorker.get_id())
    new_message = {"session_id": session_id, "messages": travel_message}
    await save_chat_history(user, new_message)
    return success("New session created successfully", new_message)




# @logger.catch()
# @route.post("/_chat_pri", summary='Send message to ChatGPT')
# async def chat_pri(user: CurrentUser = Depends(CurrentUser),
#                    message: dict = None):
#     """
#     {"messages":[{"session_id", "123", "role":"user","content":"Hello"}]}
#     """
#     request_messages = message.get("messages") or []
#     if len(request_messages) == 0:
#         return error("Message cannot be empty")
#
#     message_list = [{
#         "role": "user",
#         "content": travel_content or "Now you are a travel expert, master of travel time planning."
#     }]
#     message_list.extend(request_messages)
#
#     logger.info(f"Sending message: `{message_list}`")
#
#     # Send message and return streaming response
#     return EventSourceResponse(get_openai_stream_generator(message_list))

@logger.catch()
@route.post("/_chat_pri", summary='Send message to ChatGPT')
async def chat_pri(user: CurrentUser = Depends(CurrentUser),
                   message: dict = None):
    """
     {"session_id", "123", "role":"user", "content":"Hello"}
    """
    session_id = message.get("session_id")
    content = message.get("content")
    check_not_empty(session_id, "Session ID cannot be empty")
    check_not_empty(content, "Message content cannot be empty")

    your_message = {"role": "user", "content": content}
    logger.info(f"Sending message: `{your_message}`")

    # Get history messages
    history_message_list = await get_history_by_session_id(session_id)
    message_list = []
    for item in history_message_list:
        message_list.append(item.get("message"))
    message_list.append(your_message)

    # Save your message
    await save_chat_history(user, {
        "session_id": session_id,
        "messages": [your_message]
    })

    # Send message and return streaming response
    return EventSourceResponse(get_openai_stream_generator(message_list))

# @logger.catch()
# @route.post("/_save_pri", summary='Save message history')
# async def save(user: CurrentUser = Depends(CurrentUser),
#                message: dict = None):
#     session_id = await save_chat_history(user, message)
#     return success("Session saved successfully", {"session_id": session_id})

@logger.catch()
@route.post("/_save_pri", summary='Save message history')
async def save_pri(user: CurrentUser = Depends(CurrentUser),
                   message: dict = None):
    """
     {"session_id", "123", "role":"user","content":"Hello"}
    """
    session_id = message.get("session_id")
    content = message.get("content")
    check_not_empty(session_id, "Session ID cannot be empty")
    check_not_empty(content, "Message content cannot be empty")

    await save_chat_history(user, {
        "session_id": session_id,
        "messages": [{"role": message.get("role"), "content": content}]
    })
    return success("Session saved successfully", {"session_id": session_id})

@logger.catch()
@route.post("/history/list", summary='Get message history')
async def history(user: CurrentUser = Depends(CurrentUser),
                  params: dict = None):
    session_id = params.get("session_id") or ""
    session = new_session()
    chat_history_list = session.query(ChatHistory) \
        .filter(or_(ChatHistory.user_id == user.user_id),
                or_(ChatHistory.session_id == session_id, session_id is None or session_id == ""),
                and_(ChatHistory.is_deleted == 0)
                ) \
        .join(Relation, and_(ChatHistory.user_id == Relation.from_key,
                             ChatHistory.session_id == Relation.to_key,
                             Relation.is_deleted == 0,
                             Relation.direction == 1,
                             Relation.category == 'chat_his')) \
        .order_by(asc(ChatHistory.id)).all()
    # Filter returned fields
    filter_chat_history = [{"id": item.id,
                            "session_id": item.session_id,
                            "message": json.loads(item.content)}
                           for item in chat_history_list]

    result = []
    if len(filter_chat_history) > 0:
        sort_chat_history = sorted(filter_chat_history,
                                   key=itemgetter('session_id'))
        for key, value in groupby(sort_chat_history,
                                  key=itemgetter('session_id')):
            result.append({"session_id": key, "messages": list(value)})

    return success("Successfully retrieved", result)



