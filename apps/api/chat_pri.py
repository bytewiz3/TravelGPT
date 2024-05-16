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




load_dotenv()

# 读取应用配置
cfg = load_yaml("config/application.yaml")

# 访问超时时间
timeout = os.environ.get("OPENAI_API_TIMEOUT") or cfg.get("open_ai").get("timeout")
# API_KEY
api_key = os.environ.get("OPENAI_API_KEY") or cfg.get("open_ai").get("api_key")
# 系统内容
sys_content = os.environ.get("OPENAI_API_SYS_CONTENT") or cfg.get("open_ai").get("sys_content")
# 旅游内容
travel_content = os.environ.get("OPENAI_API_TRAVEL_CONTENT") or cfg.get("open_ai").get("travel_content")
# 使用模型
model = os.environ.get("OPENAI_API_MODEL") or cfg.get("open_ai").get("model")
# 代理
proxy = os.environ.get("OPENAI_API_PROXY") or cfg.get("open_ai").get("proxy") or None
# 带代理的客户端
http_client = httpx.Client(proxy=proxy) if proxy else httpx.Client()


