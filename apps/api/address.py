# -*- coding: utf-8 -*- 
 
from apps.api.base import error, success, check_not_empty 
from apps.base.log import logger 
from fastapi import APIRouter 
from dotenv import load_dotenv 
 
from common.utils import load_yaml 
from common.utils.amap_utils import gaode, circum_address 
from common.utils.hanlp_utils import select_address 
 
route = APIRouter() 
 
load_dotenv() 
 
# Read application configuration 
cfg = load_yaml("config/application.yaml") 
 
 
@logger.catch() 
@route.post("/address_list", summary='Get address information based on content') 
async def address_list(params: dict): 
    contents = params.get("messages") or [] 
    if len(contents) != 2: 
        return error("Your parameters are incorrect") 
 
    logger.info(f"Message Q&A content: `{contents}`") 
 
    question = contents[0] 
    answer = contents[1] 
 
    site_list = select_address(question) 
    address_list = select_address(answer) 
 
    return success(await address_parser(site_list, address_list)) 
 
 
@logger.catch() 
@route.post("/circum_address_list", summary='Get surrounding information based on content') 
async def circum_address_list(params: dict): 
    address_name = params.get("address_name") or "" 
    check_not_empty(address_name) 
    return success(await circum_address(address_name)) 
 
 
async def address_parser(site_list: set, address_list: set): 
    # Add prefix to addresses for more accurate positioning 
    pre_name = site_list.pop() if len(site_list) == 1 else "" 
 
    merge_addr_with_url = [] 
    for addr in address_list: 
        # Use 'Gaode Maps' to query the latitude and longitude of the address 
        addr_local, annotate_url = await gaode(pre_name, addr) 
        addr_local["annotate_url"] = annotate_url 
        merge_addr_with_url.append(addr_local) 
    return merge_addr_with_url 
