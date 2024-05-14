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

