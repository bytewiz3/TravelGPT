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

venv = 'Development Environment' if fastapi_env else 'Production Environment'


class BaseConfig(BaseModel):
    VERSION: str = '1.0.0'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    SECRET_KEY: str = '-*&^)()sd(*A%&^aWEQaasda_asdasd*&*)(asd%$#'
    # Document address, can be disabled in production None
    DOCS_URL: str = "/docs"
    # Document-related request data interface, can be disabled in production None
    OPENAPI_URL: str = "/openapi.json"
    # Disable redoc document
    REDOC_URL: str = "/redoc"
    # Environment name
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
#     docs = f'API Documentation: http://{config.host}:{config.port}{config.DOCS_URL}'
#     config.ENV = "Development Environment"
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
        logger.exception("Configuration file error!")


pconf = parserconf()
conf = Config(**dict(pconf.items('comm')))

mysqlconf = Database(**dict(pconf.items('mysql')))
pgdbconf = Database(**dict(pconf.items('postgresql')))
LogLevel = "DEBUG" if conf.debug else "INFO"
