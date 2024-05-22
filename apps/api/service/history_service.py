# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from apps.api.base import error, success, check_not_empty, check_duplicate, \
    check_user, check_true, check_pwd, check_email
from apps.api.service.user_service import find_user
from apps.base.exceptions import AuthError, ServerError
from apps.base.log import logger

from apps.base.conf import templates, conf
import jwt
from apps.models import Users, LoginHistory, AccessRecord
from apps.base.db import new_session
from fastapi import Header, Request, APIRouter, Body
import time
from apps.base.middleware import ToLogin
from common.utils import get_now, now_format_to_str, load_yaml
from sqlalchemy import or_

# from common.utils.aes_utils import aes_encrypt, aes_decrypt
from common.utils.email_utils import send_email
from common.utils.redis_utils import RedisUtils
from common.utils.string_utils import random_str
from common.utils.md5_utils import md5

route = APIRouter()
Templ = templates.TemplateResponse

# 读取应用配置
cfg = load_yaml("config/application.yaml")
reset_pwd_cfg = cfg.get("reset_pwd")
reset_pwd_url = os.environ.get("RESET_PWD_URL") or reset_pwd_cfg.get("url")
# reset_pwd_salt = os.environ.get("RESET_PWD_SALT") or reset_pwd_cfg.get("salt")


@logger.catch()
@route.post("/_login", summary='用户登录，获取TOKEN')
def login(request: Request,
          username: str = Body(...),
          passwd: str = Body(...), ):
    logger.debug(f"{username} 用户登录中...")
    session = new_session()
    user = session.query(Users).filter_by(username=username,
                                          passwd=md5(passwd)).first()
    if not user:
        return error("登录失败! 用户不存在或密码不正确!", -1)

    logger.debug(user)

    user.last_login = get_now()
    login_ip = request.client.host
    info = {
        "user_id": user.user_id,
        "username": user.username,
        "nickname": user.nickname,
        "roles": ['admin'],
        "photo": 'static/photo/head.jpg',
        "login_ip": login_ip,
        "last_login": now_format_to_str('%Y-%m-%d %H:%M:%S'),
        "token": ""
    }
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        'iss': 'travel_gpt',  # token签发者
        'data': info,
        "jti": "4f1g23a12aa"
    }
    # 生成token
    info["token"] = jwt.encode(payload, conf.SECRET_KEY, algorithm='HS512', )
    #  增加登录历史记录
    login_history = LoginHistory(username=user.username,
                                 nickname=user.nickname,
                                 phone=user.phone,
                                 email=user.email,
                                 login_ip=login_ip)
    session.add(login_history)

    session.commit()
    session.flush()
    session.close()

    return success("登录成功!", info)


@logger.catch()
@route.post("/_register", summary='用户注册')
def register(request: Request,
             username: str = Body(...),
             passwd: str = Body(...),
             nickname: str = Body(default=None),
             phone: str = Body(default=None),
             email: str = Body(default=None)):
    check_email(email)
    check_user(username)
    check_pwd(passwd)

    session = new_session()
    user = session.query(Users).filter(or_(Users.username == username,
                                           Users.phone == (phone or '$$$$$$'),  # 不存在的字符串，作为条件
                                           Users.email == (email or '$$$$$$'),  # 不存在的字符串，作为条件
                                           )).first()
    check_duplicate(user, "用户已经存在!")

    user = Users(username=username, nickname=nickname, status=1)
    user.passwd = md5(passwd)
    user.phone = phone
    user.email = email

    session.add(user)
    session.commit()
    session.flush()

    return success("用户注册成功!")


@logger.catch()
@route.post("/_find_pwd", summary='找回密码')
def find_pwd(request: Request,
             username: str = Body(...),
             email: str = Body(default=None)):
    check_email(email)
    check_user(username)

    user = find_user(username, email)
    check_not_empty(user, "用户不存在,请重新输入")

    # 邮箱
    email = user.email

    # aes加密后的KEY
    reset_pwd_salt = random_str(32)
    encrypt_key = aes_encrypt(reset_pwd_salt, username + "^^" + email)
    RedisUtils.set("reset_pwd:" + encrypt_key, "1")
    RedisUtils.set("reset_pwd:" + encrypt_key + ":rnd_str", reset_pwd_salt)

    url = f"{reset_pwd_url}?reset_key={encrypt_key}"
    is_send = send_email("找回密码", f"通过下面的链接，找回您的密码! \r\n {url}", email)
    return success("已发送邮件，请通过邮箱找回密码!") if is_send else error("发送邮件失败!")


@logger.catch()
@route.post("/_find_modify_pwd", summary='找回修改密码')
def find_modify_pwd(request: Request,
                    reset_key: str = Body(...),
                    new_pwd: str = Body(...),
                    repeat_new_pwd: str = Body(...)):
    check_not_empty(reset_key, "找回密码Key不能为空")
    check_pwd(new_pwd)

    check_not_empty(new_pwd, "新的密码")
    check_not_empty(repeat_new_pwd, "重复新的密码")
    check_true(new_pwd == repeat_new_pwd, "请确认输入的密码是否一致")

    is_exists = RedisUtils.exists("reset_pwd:" + reset_key)
    check_true(is_exists, "找回密码Key已失效，请重新找回密码!")

    # 解密
    try:
        reset_pwd_salt = RedisUtils.get("reset_pwd:" + reset_key + ":rnd_str")
        user_email = aes_decrypt(reset_pwd_salt.decode(), reset_key)
    except Exception as e:
        logger.error(e)
        return error("找回密码Key已失效，请重新找回密码!")

    username, email = user_email.split("^^")
    session = new_session()
    try:
        ret = session.query(Users) \
            .filter(or_(Users.username == (username or '$$$$$$'),
                        Users.email == (email or '$$$$$$'))) \
            .update({"passwd": md5(new_pwd), "gmt_modified": datetime.now()}, synchronize_session=False)
        session.commit()
        if ret:
            RedisUtils.delete("reset_pwd:" + reset_key)
            RedisUtils.delete("reset_pwd:" + reset_key + ":rnd_str")
            return success("密码修改成功!")
    except Exception as e:
        print(e)
        session.rollback()
        return error("密码修改成功失败", 501)


@logger.catch()
class User_info:
    def __init__(self, userid):
        self.USERID = userid


class CurrentUser:
    def __init__(self, request: Request, token: str = Header(None)):

        if not request:
            self.user_id = "-1"
            self.username = "匿名用户"
            self.nickname = "匿名用户"
            return

        if not token:
            raise AuthError('用户未登录!')

        try:
            users = jwt.decode(token, conf.SECRET_KEY, algorithms=['HS512'])
        except Exception as e:
            logger.error(e)
            raise ServerError(e.args[0], 401)

        if not users:
            raise ServerError("登录Token校验异常")

        user = users.get('data')
        if not user:
            raise ServerError("登录Token校验异常")

        logger.debug(user)

        self.user_id = user.get("user_id")
        self.username = user['username']
        self.nickname = user['nickname']
        self.login_ip = user['login_ip']

        if cfg["travel_gpt"].get("access_record"):
            access_records = AccessRecord(user_id=user.get("user_id"),
                                          username=user['username'],
                                          nickname=user['nickname'],
                                          url=str(request.url),
                                          method=request.method)
            session = new_session()
            session.add(access_records)
            session.commit()
        return


@logger.catch()
@route.get("/login", summary='用户登录web')
def login(request: Request):
    context = {'request': request, }
    return Templ('login.html', context)


class CurrentUserRedir:
    def __init__(self, request: Request, TOKEN: str = Header(None), QTOKEN: str = None):
        if TOKEN or QTOKEN:
            tk = TOKEN if TOKEN else QTOKEN
            users = ''
            try:
                users = jwt.decode(tk, conf.SECRET_KEY, algorithms=['HS512'])
            except Exception as e:
                logger.error(e)
            if users:
                user = users['data']
                logger.debug(user)
                self.userid = user['id']
                self.username = user['username']
                self.nicename = user['nicename']
                # logger.debug(conf.access_records)
                if conf.access_records:
                    accessrecords = AccessRecords(userid=user['id'], username=user['username'],
                                                  nicename=user['nicename'], url=str(request.url),
                                                  method=request.method)
                    # logger.debug(accessrecords.nicename)
                    session = new_session()
                    session.add(accessrecords)
                    # session.commit()
                return
        else:
            raise ToLogin(url='/login')
