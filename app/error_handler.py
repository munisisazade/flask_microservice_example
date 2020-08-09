import traceback
import http
from flask import current_app, request
from .helpers.logger import log
from .helpers.parser import unique_error_msg_parser
from mongoengine.errors import NotUniqueError, ValidationError
from cerberus.validator import DocumentError
from .response import Error, PageNotFound, MethodNotAllowed


@current_app.errorhandler(NotUniqueError)
def not_unique_handler(e):
    msg = unique_error_msg_parser(str(e))
    return Error(status=409, message={
        "code": 409,
        "message": msg
    }).to_response()


@current_app.errorhandler(DocumentError)
def body_validation_error(e):
    return Error(status=400, message={
        "code": 400,
        "message": "Bad request"
    }).to_response()


@current_app.errorhandler(ValidationError)
def body_validation_error(e):
    return Error(status=400, message={
        "code": 400,
        "message": str(e)
    }).to_response()


@current_app.errorhandler(400)
def json_decode_error(e):
    return Error(status=400, message={
        "code": 400,
        "message": "Bad request"
    }).to_response()


# error 404 urls
@current_app.errorhandler(404)
def page_not_found(e):
    """
        If server could not find what was requested.
        Store request ip address and object data to log files.
    """
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(",")[0]
    else:
        ip = request.remote_addr
    log.error("Page not found at {} {} {}".format(request.path, request.method, ip))
    return PageNotFound().to_response()


# error 405 urls
@current_app.errorhandler(405)
def method_not_allowed(e):
    """
        The 405 Method Not Allowed is an HTTP response
        status code indicating that server has rejected
        that particular method for the requested resource.
        Store object logs to log files.
    """
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(",")[0]
    else:
        ip = request.remote_addr
    log.error("Method not allowed at {} {} {}".format(request.path, request.method, ip))
    return MethodNotAllowed().to_response()


@current_app.errorhandler(Exception)
def exceptions(e):
    """
        When an error occurs within a method,
        the method creates an object and hands it off to the runtime system.
        Contains information about the error,
        including its type and the state of the program when the error occurred.
        Store object logs to log files.
    """
    tb = traceback.format_exc()
    log.fatal(f"{tb}")
    return Error(status=500, message={"message": "Something unexpected happened."}).to_response()
