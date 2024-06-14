# -*- coding: utf-8 -*- 
import os 
import sys 
 
import uvicorn 
from apps.base.hello import hello, logger 
from apps.base.conf import conf, LogLevel 
from apps.route import create_app 
 
root_path = os.getcwd() 
sys.path.append(root_path) 
 
abs_path = "" 
if getattr(sys, 'frozen', False): 
    abs_path = os.path.dirname(os.path.abspath(sys.executable)) 
elif __file__: 
    abs_path = os.path.dirname(os.path.abspath("travelgpt")) 
 
app = create_app() 
if __name__ == "__main__": 
    log_config = { 
        "version": 1, 
        "disable_existing_loggers": "false", 
        "formatters": { 
            "default": { 
                "()": "uvicorn.logging.DefaultFormatter", 
                "fmt": "%(levelprefix)s %(message)s" 
            }, 
            "access": { 
                "()": "uvicorn.logging.AccessFormatter", 
                "fmt": "%(asctime)s | %(levelprefix)s |%(client_addr)s - \"%(request_line)s\" %(status_code)s" 
            } 
        }, 
        "handlers": { 
            "default": { 
                "formatter": "default", 
                "class": "logging.StreamHandler", 
                "stream": "ext://sys.stderr" 
            }, 
            "access": { 
                "formatter": "access", 
                "class": "logging.StreamHandler", 
                "stream": "ext://sys.stdout" 
            } 
        }, 
        "loggers": { 
            "uvicorn": { 
                "handlers": [ 
                    "default" 
                ], 
                "level": "DEBUG" 
            }, 
            "uvicorn.error": { 
                "level": "DEBUG" 
            }, 
            "uvicorn.access": { 
                "handlers": [ 
                    "access" 
                ], 
                "level": "DEBUG", 
                "propagate": "false" 
            }, "sqlalchemy.engine": { 
                "level": "DEBUG" 
            } 
        } 
    } 
    try: 
        name_app = os.path.basename(__file__)[0:-3] 
        print("App Directory:::::", os.getcwd()) 
        hello() 
        uvicorn.run(app=f'{name_app}:app', 
                    host=conf.host, 
                    port=conf.port, 
                    reload=False, 
                    log_level=LogLevel.lower(), 
                    log_config=log_config 
                    ) 
    except Exception as e: 
        logger.exception("Service Internal Error!", e) 
