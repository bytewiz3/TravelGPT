import errno 
import json 
import os 
import sys 
 
import yaml 
 
from common.utils import ENV 
 
# Whether it is an executable file 
is_exe = ENV.is_exe() 
 
 
def load_text(cfg_path): 
    """ 
        Current execution script path 
        module_path = os.path.dirname(__file__) 
        filename = module_path + '../test.txt' 
        read_file_text(filename) 
    """ 
    with open(cfg_path, encoding='utf-8') as fi: 
        fi.seek(0) 
        return fi.read() 
 
 
def load_json(cfg_path): 
    file_exist_on_error(cfg_path) 
    with open(cfg_path, encoding='utf-8') as fi: 
        fi.seek(0) 
        return json.loads(fi.read()) 
 
 
def load_yaml(cfg_path: object) -> object: 
    path = get_real_path(cfg_path) 
    file_exist_on_error(path) 
    with open(path, encoding='utf-8') as f: 
        return yaml.safe_load(f) 
 
def file_exist(relative_file_path): 
    if os.path.exists(relative_file_path): 
        return True 
    return False 
 
 
def file_exist_on_error(relative_file_path): 
    if not file_exist(relative_file_path): 
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), relative_file_path) 
 
 
def get_real_path(file): 
    if is_exe: 
        cmd = os.path.abspath(os.path.dirname(sys.executable)) 
    else: 
        cmd = os.path.dirname(__file__) + "/../../" 
    return os.path.join(cmd, file) 
