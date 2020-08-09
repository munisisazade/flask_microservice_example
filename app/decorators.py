import time
from functools import wraps
import requests
from cerberus import Validator
from flask import request, current_app

from .response import Error
from .helpers.logger import log
from .helpers.urlparser import url_parse


def login_required(func):
    def wrapper(*args, **kwargs):
        # Authorization header
        return func(*args, **kwargs)
    return wrapper


def form_validation(schema, get=False):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            v = Validator(schema)
            if v.validate(request.json if not get else request.args):
                return func(*args, **kwargs)
            return Error(status=422, message={
                "message": "Form düzgün deyil.",
                "data": v.errors
            }).to_response()
        return wrapper
    return actual_decorator




