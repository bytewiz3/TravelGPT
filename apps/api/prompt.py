# -*- coding: utf-8 -*-
import datetime
from datetime import time
from time import sleep

from sqlalchemy import and_, asc

from apps.api.base import error, success, check_not_empty, check_not_empty_list
from apps.api.user.user import CurrentUser
from apps.base.db import new_session
from apps.base.log import logger
from fastapi import APIRouter, Depends
from dotenv import load_dotenv

from apps.models import Prompt
from common.utils import load_yaml

route = APIRouter()

load_dotenv()

# Read application configuration
cfg = load_yaml("config/application.yaml")


@logger.catch()
@route.post("/list", summary='Get Prompt list')
async def get_list(params: dict = None):
    category = params.get("category")
    check_not_empty(category, "Category cannot be empty")

    session = new_session()
    prompt_list = session.query(Prompt.prompt_id, Prompt.act, Prompt.prompt) \
        .filter(and_(Prompt.category == category),
                and_(Prompt.is_deleted == 0)) \
        .order_by(asc(Prompt.id)).all()
    return success("Successfully retrieved", prompt_list)


@logger.catch()
@route.post("/_add", summary='Add Prompt')
async def add(user: CurrentUser = Depends(CurrentUser),
              params: dict = None):
    prompt = Prompt()
    prompt.category = params.get("category")
    prompt.act = params.get("act")
    prompt.prompt = params.get("prompt")
    prompt.creator = user.username
    prompt.modifier = user.username

    session = new_session()
    session.add(prompt)
    session.commit()
    session.flush()
    return success("Success")


@logger.catch()
@route.post("/_delete", summary='Delete Prompt')
async def delete(user: CurrentUser = Depends(CurrentUser),
                 params: dict = None):
    id_list = params.get("id_list") or []
    check_not_empty_list(id_list, "Prompt ID cannot be empty")

    session = new_session()
    try:
        session.query(Prompt) \
            .filter(Prompt.id.in_(id_list)) \
            .filter(Prompt.is_deleted == 0) \
            .update({"is_deleted": 1, "modifier": user.username,
                     "gmt_modified": datetime.datetime.now()}, synchronize_session=False)
    except Exception as e:
        print(e)
        session.rollback()
        return error("Failed to delete Prompt", 501)
    session.commit()
    return success("Successfully deleted Prompt")


@logger.catch()
@route.post("/_update", summary='Update Prompt')
async def update(user: CurrentUser = Depends(CurrentUser),
                 params: dict = None):
    id_key = params.get("id")
    check_not_empty(id_key, "Prompt ID cannot be empty")

    category = params.get("category")
    act = params.get("act")
    prompt = params.get("prompt")

    session = new_session()
    try:
        session.query(Prompt) \
            .filter(Prompt.id == id_key) \
            .filter(Prompt.is_deleted == 0) \
            .update({"category": category, "act": act, "prompt": prompt,
                     "gmt_modified": datetime.datetime.now()}, synchronize_session=False)
    except Exception as e:
        print(e)
        session.rollback()
        return error("Failed to update Prompt", 501)
    session.commit()
    return success("Successfully updated Prompt")
