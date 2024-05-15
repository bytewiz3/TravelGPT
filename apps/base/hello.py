# -*- coding: utf-8 -*-
"""
@Time ： 2021/12/29 16:19
@Auth ： Jolg
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
        print(f"基础参数：{conf}")
        print(f"数据库：{mysqlconf}")
        docs = f'接口文档 :  http://{conf.host}:{conf.port}{conf.DOCS_URL}'
    txt = f'''============================================================================

            项目名称 :  {conf.title}           
            开发人员 :  waj
            开发时间 :  2024-04-01 
            当前版本 :  {conf.VERSION}
            {docs}
            启动环境 :  {conf.ENV}  |  DEBUG: {conf.debug}   |    日志级别 {LogLevel}            
============================================================================'''
    print(txt)
    logger.info("启动成功！")
