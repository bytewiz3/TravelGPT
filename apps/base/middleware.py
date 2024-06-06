# -*- coding: utf-8 -*-
"""
@Time ： 2024/07/10 11:36
@Auth ： Yijie Weng
@File ：middleware.py
@IDE ：PyCharm

"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def register_cors(app: FastAPI):
    """
    Enable cross-origin resource sharing (CORS).
    """
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=['http://localhost:8081'],  # Works, but the Vue.js local port keeps changing. It might not always be this port when giving the API to others.
        # allow_origins=['*'],   # Invalid bug: allow_origins=['http://localhost:8081']
        allow_origin_regex='https?://.*',  # Changed to use regular expressions
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# Author: Yijie Weng
# File: middle_regedit.py
# Date: 2023/07/09 19:51
# Development Tool: PyCharm
import traceback

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from apps.base.log import logger
from starlette.responses import RedirectResponse


class PostParamsError(Exception):
    def __init__(self, err_desc: str = "POST request parameter error"):
        self.err_desc = err_desc


class TokenAuthError(Exception):
    def __init__(self, err_desc: str = "Token authentication failed"):
        self.err_desc = err_desc


class ToLogin(Exception):
    def __init__(self, url: str = "/login"):
        self.url = url


class UnicornException(Exception):
    def __init__(self, url: str):
        self.url = url


def register_exception(app: FastAPI):
    """
    Global exception handling
    """

    @app.exception_handler(ToLogin)
    async def unicorn_exception_handler(request: Request, exc: ToLogin):
        # return JSONResponse(
        #     status_code=418,
        #     content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
        # )
        return RedirectResponse(url=exc.url)


def register_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=['http://localhost:8081'],  # Works, but the Vue.js local port keeps changing. It might not always be this port when giving the API to others.
        # allow_origins=['*'],   # Invalid bug: allow_origins=['http://localhost:8081']
        allow_origin_regex='https?://.*',  # Changed to use regular expressions
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_middleware(app: FastAPI):
    """
    Request-response interception hook

    https://fastapi.tiangolo.com/tutorial/middleware/
    :param app:
    :return:
    """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        # logger.info(f"Access Record:{request.method} url:{request.url}==headers:{request.headers.get('user-agent')}==IP:{request.client.host}")
        logger.info(f"|Access Record:{request.method}  |url:{request.url}  |IP:{request.client.host}")
        # logger.info(f"|Access Record:{dir(request)}")
        # logger.info(f"|Access Record:{request.headers}")
        response = await call_next(request)
        return response
