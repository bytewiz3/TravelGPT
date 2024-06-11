import pypyodbc 
import logging 
 
from common.utils import file_utils, get_real_path 
 
cfg_path = get_real_path('config/db_config.json') 
db_config = file_utils.load_json(cfg_path) 
 
 
class DBUtils: 
 
    def __init__(self): 
        self.host = db_config["db.host"] 
        self.username = db_config["db.username"] 
        self.password = db_config["db.password"] 
        self.db = db_config["db.source"] 
        self.charset = db_config["db.charset"] 
        self.conn = None 
        self.cur = None 
        self.procedure = db_config["db.procedure"].split(",") 
 
    def connect(self): 
        if not self.conn: 
            self.conn = pypyodbc.connect(driver='{SQL Server}', 
                                         server=self.host, 
                                         database=self.db, 
                                         uid=self.username, 
                                         pwd=self.password) 
            if self.conn: 
                logging.info("Database connected successfully!") 
            else: 
                logging.error("Database connection failed!") 
            self.cur = self.conn.cursor() 
        return self.conn 
 
    def insert(self, sql, data): 
        self.cur.executemany(sql, data) 
 
    def select(self, sql, args): 
        self.cur.execute(sql, args) 
        return self.cur.fetchall() 
 
    def process(self, name, args, size=None): 
        # self.cur.callproc(name, args) 
        result = [] 
 
        self.cur.execute(name, args) 
        desc = self.cur.description 
        if size: 
            res = self.cur.fetchmany(size) 
            result.append(res) 
        else: 
            res = self.cur.fetchall() 
            result.append(res) 
 
        # Fetch the second result set 
        self.next_res(result, size) 
        data_dict = [] 
        for r in result: 
            data_dict.append([dict(zip([col[0] for col in desc], row)) for row in r]) 
        return data_dict 
 
    def next_res(self, result, size=None): 
        if self.cur.nextset(): 
            if size: 
                res = self.cur.fetchmany(size) 
                result.append(res) 
            else: 
                res = self.cur.fetchall() 
                result.append(res) 
 
 
    def rollback(self): 
        if self.conn: 
            self.conn.rollback() 
        self.close_connect() 
 
    def close_connect(self): 
        if self.cur: 
            self.cur.close() 
 
        if self.conn: 
            self.conn.close() 
