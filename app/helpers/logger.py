import json
from datetime import datetime
from inspect import getframeinfo, stack
from flask import current_app as app

LOG_LEVELS = [
    "FATAL",
    "ERROR",
    "WARNING",
    "INFO",
    "DEBUG"
]


class MainLogger(object):
    log_file = app.config['LOG_FILE_PATH']

    @classmethod
    def get_format(cls, info, level, msg):
        log_data = {
            "app": app.config["APP_NAME"],
            "@timestamp": datetime.now().isoformat(),
            "level": level,
            "function": info.function,
            "file": info.filename.split('/')[-1],
            "line": info.lineno,
            "message": msg
        }
        return json.dumps(log_data)

    @classmethod
    def error(cls, msg):
        caller = getframeinfo(stack()[1][0])
        data = cls.get_format(caller, LOG_LEVELS[1], msg)
        cls.__write(data)

    @classmethod
    def fatal(cls, msg):
        caller = getframeinfo(stack()[1][0])
        data = cls.get_format(caller, LOG_LEVELS[0], msg)
        cls.__write(data)

    @classmethod
    def warning(cls, msg):
        caller = getframeinfo(stack()[1][0])
        data = cls.get_format(caller, LOG_LEVELS[2], msg)
        cls.__write(data)

    @classmethod
    def info(cls, msg):
        caller = getframeinfo(stack()[1][0])
        data = cls.get_format(caller, LOG_LEVELS[3], msg)
        cls.__write(data)

    @classmethod
    def debug(cls, msg):
        caller = getframeinfo(stack()[1][0])
        data = cls.get_format(caller, LOG_LEVELS[4], msg)
        cls.__write(data)

    @classmethod
    def __write(cls, data):
        print(data)
        with open(cls.log_file, "a") as file:
            file.write(f"{data}\n")


log = MainLogger
