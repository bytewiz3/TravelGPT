# -*- coding: utf-8 -*-
import uvicorn
from apps.base.hello import hello, logger
from apps.base.conf import conf, LogLevel
from apps.route import create_app

app = create_app()
if __name__ == "__main__":
    try:
        hello()
        uvicorn.run(app='runme:app',
                    host=conf.host,
                    port=conf.port,
                    reload=True,
                    log_level=LogLevel.lower(),
                    log_config="apps/base/log_conf.json"
                    )
    except Exception as e:
        logger.exception("Service Exception!", e)
