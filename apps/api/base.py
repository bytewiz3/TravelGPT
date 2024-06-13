from apps.base.exceptions import CheckError, CheckDuplicate 
 
 
def error(msg='', code=400): 
    return {'msg': msg, 'code': code or 400, 'data': ''} 
 
 
def success(msg='', data=''): 
    return {'msg': msg, 'code': 0, 'data': data} 
 
 
def check_not_empty(data='', msg=''): 
    if not data: 
        raise CheckError(msg) 
 
 
def check_not_empty_any_one(d1='', d2='',  msg=''): 
    if d1 and d2: 
        raise CheckError(msg) 
 
 
def check_duplicate(data, msg=''): 
    if data: 
        raise CheckDuplicate(msg) 
 
 
def check_not_empty_list(data='', msg=''): 
    if len(data or []) == 0: 
        raise CheckError(msg) 
