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

# 读取应用配置
cfg = load_yaml("config/application.yaml")


@logger.catch()
@route.post("/address_list", summary='根据内容获取地址信息')
async def address_list(params: dict):
    contents = params.get("messages") or []
    if len(contents) != 2:
        return error("您的参数有误")

    logger.info(f"消息问答内容 `{contents}`")

    question = contents[0]
    answer = contents[1]

    site_list = select_address(question)
    address_list = select_address(answer)

    return success(await address_parser(site_list, address_list))


@logger.catch()
@route.post("/circum_address_list", summary='根据内容获取周边信息')
async def circum_address_list(params: dict):
    address_name = params.get("address_name") or ""
    check_not_empty(address_name)
    return success(await circum_address(address_name))


async def address_parser(site_list: set, address_list: set):
    # 地址加前缀，更加精确地定位
    pre_name = site_list.pop() if len(site_list) == 1 else ""

    merge_addr_with_url = []
    for addr in address_list:
        # 使用`高德地图`查询地址的经纬度
        addr_local, annotate_url = await gaode(pre_name, addr)
        addr_local["annotate_url"] = annotate_url
        merge_addr_with_url.append(addr_local)
    return merge_addr_with_url
