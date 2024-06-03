# -*- coding: utf-8 -*- 
import pymysql 
from dotenv import load_dotenv 
 
from common.utils import load_yaml 
from sqlalchemy import create_engine 
import os 
from sqlalchemy.orm import sessionmaker 
 
load_dotenv() 
pymysql.install_as_MySQLdb() 
 
# Read application configuration
cfg = load_yaml("config/application.yaml") 
# Access timeout 
db_type = os.environ.get("DATA_SOURCE_TYPE") or cfg.get("data_source").get("type") 
db_url = os.environ.get("DATA_SOURCE_URL") or cfg.get("data_source").get(f"{db_type}_url") 
db_debug = os.environ.get("DATA_SOURCE_LOG_LEVEL") or cfg.get("data_source").get("log_level") 
 
engine = create_engine(db_url, echo=db_debug, pool_recycle=60 * 5) 
 
 
def new_session(): 
    db_session = sessionmaker(bind=engine) 
    return db_session() 
