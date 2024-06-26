import datetime 
import time 
 
 
def now_format_to_str(fmt=None): 
    fmt = fmt or '%Y%m%d%M%I%S' 
    return time.strftime(fmt, time.localtime()) 
 
 
def get_timestamp(): 
    return get_now().isoformat("T", "milliseconds") + "Z" 
 
 
def get_now(): 
    return datetime.datetime.now() 
