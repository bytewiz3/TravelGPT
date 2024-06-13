# -*- coding: utf-8 -*- 
from apps.base.log import logger 
from apps.base.conf import templates 
from fastapi import APIRouter, Request 
 
route = APIRouter() 
Templ = templates.TemplateResponse 
 
 
@logger.catch() 
@route.get("/index", summary='') 
def login(request: Request): 
    context = {'request': request, } 
    return Templ('index.html', context) 
