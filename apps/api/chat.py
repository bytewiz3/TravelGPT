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


