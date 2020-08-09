import os
from dotenv import load_dotenv
from pymongo import uri_parser

load_dotenv()
load_dotenv(dotenv_path='.secret.env')


def env_to_python(string):
    """
        Convert enviroment varible to Python object
    """
    if string.strip().capitalize() == "False":
        return False
    elif string.strip().capitalize() == "True":
        return True
    else:
        return string


def get_db_name_from_uri(mongo_uri):
    """
        Parse Mongo Uri find database name
    """
    parsed = uri_parser.parse_uri(mongo_uri)
    return parsed["database"]


class Config(object):
    # Flask default configs
    ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = env_to_python(os.getenv("DEBUG", "True"))
    TESTING = env_to_python(os.getenv("TESTING", "True"))
    CSRF_ENABLED = env_to_python(os.getenv("CSRF_ENABLED", "True"))
    FLASK_APP = os.getenv("FLASK_APP", "run.py")
    SECRET = os.getenv("SECRET", "q&-=9#$8a5cy297l1qkb+$8o)h(3a$2br!8tdo5iz6rb@ub2=-")
    TEMPLATES_AUTO_RELOAD = env_to_python(os.getenv("TEMPLATES_AUTO_RELOAD", "True"))
    # aditional config loads here
    URL_PREFIX = os.getenv("URL_PREFIX", "/api/v1/")
    MONGODB_SETTINGS = {
        'db': get_db_name_from_uri(
            os.getenv("MONGO_URL", "mongodb://bridge_user:TC6eHtutV6U488r8ugav95S93d6AzJh6Aab@localhost:27017/bridge")),
        'host': os.getenv("MONGO_URL",
                          "mongodb://bridge_user:TC6eHtutV6U488r8ugav95S93d6AzJh6Aab@localhost:27017/bridge")
    }
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "272y38dh34dwjenjanskfjnsdjkfnsd")
    JWT_HEADER_TYPE = os.getenv("JWT_HEADER_TYPE", "Token")
    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "microservice.log")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = os.getenv("PORT", 5010)
    APP_NAME = os.getenv("APP_NAME", "microservice")
    PYDOC = os.getenv("PYDOC", False)
