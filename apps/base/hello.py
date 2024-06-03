# -*- coding: utf-8 -*-
"""
@Time ： 2023/06/14 16:19
@Auth ： Yijie Weng
@File ：hello.py
@IDE ：PyCharm

"""

from apps.base.conf import conf, mysqlconf, LogLevel, pgdbconf
from apps.base.log import initlog
from apps.base.log import logger
from apps.models import initdb


@logger.catch()
def hello():
    initlog()
    initdb()
    if conf.debug:
        print(f"Basic parameters: {conf}")
        print(f"Database: {mysqlconf}")
        docs = f'API documentation: http://{conf.host}:{conf.port}{conf.DOCS_URL}'
    txt = f'''============================================================================

            Project Name :  {conf.title}           
            Developer :  Yijie Weng
            Development Date :  2023-06-14 
            Current Version :  {conf.VERSION}
            {docs}
            Environment :  {conf.ENV}  |  DEBUG: {conf.debug}   |    Log Level {LogLevel}            
============================================================================'''
    print(txt)
    logger.info("Startup successful！")
