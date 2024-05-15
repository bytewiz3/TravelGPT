# -*- coding: utf-8 -*-

from pydantic import BaseModel
import os, sys
from configparser import ConfigParser, RawConfigParser
from typing import Optional
from pathlib import Path
from starlette.templating import Jinja2Templates
from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent.parent
fastapi_env = os.environ.get('FASTAPI_ENV')
# fastapi_env=None

venv = '开发环境' if fastapi_env else '生产环境'


class BaseConfig(BaseModel):
    VERSION: str = '1.0.0'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 天
    SECRET_KEY: str = '-*&^)()sd(*A%&^aWEQaasda_asdasd*&*)(asd%$#'
    # 文档地址 成产环境可以关闭 None
    DOCS_URL: str = "/docs"
    # # 文档关联请求数据接口 成产环境可以关闭 None
    OPENAPI_URL: str = "/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: str = "/redoc"
    # 环境名称
    ENV: str = venv
    access_records: bool = False


class Database(BaseModel):
    host: str
    port: int = 3306
    dbname: str
    username: str
    password: str


class Config(BaseConfig):
    debug: bool = False
    title: str = ''
    description: str = ''

    port: int = 8080
    host: str = '0.0.0.0'
    db: str = 'sqlite'


# if fastapi_env:
#     config.DOCS_URL = "/docs"
#     config.OPENAPI_URL = "/openapi.json"
#     config.REDOC_URL = "/redoc"
#     docs = f'接口文档 :  http://{config.host}:{config.port}{config.DOCS_URL}'
#     config.ENV = "开发环境"
# if config.debug:
#     config.LOGLEVEL = "DEBUG"

templates = Jinja2Templates(directory="apps/templates")


@logger.catch()
def parserconf():
    try:
        parserconfig = RawConfigParser()
        conffile = 'conf.ini' if fastapi_env else 'conf.ini'
        configfile = os.path.join(BASE_DIR, conffile)
        parserconfig.read(configfile, encoding='utf-8')
        parserconfig.items('comm')
        parserconfig.items('mysql')
        return parserconfig
    except:
        logger.exception("配置文件错误！")


pconf = parserconf()
conf = Config(**dict(pconf.items('comm')))

mysqlconf = Database(**dict(pconf.items('mysql')))
pgdbconf = Database(**dict(pconf.items('postgresql')))
LogLevel = "DEBUG" if conf.debug else "INFO"
