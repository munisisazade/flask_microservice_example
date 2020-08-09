import uuid
from datetime import datetime
from http import HTTPStatus
from flask import current_app, jsonify


class Response(object):
    APP_NAME = current_app.config['APP_NAME']

    def __init__(self, status, message, transaction=None):
        self.status = status
        self.description = HTTPStatus(self.status).phrase
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transaction = str(uuid.uuid4()) if not transaction else transaction
        self.app_name = self.APP_NAME
        self.message = message

    def to_response(self):
        return jsonify(self.serialize()), self.status


class Success(Response):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def serialize(self):
        return {
            'timestamp': self.timestamp,
            'status': self.status,
            'description': HTTPStatus(self.status).phrase,
            'transaction': self.transaction,
            'exception': None,
            'app_name': self.app_name,
            'data': self.message
        }


class Error(Response):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def serialize(self):
        return {
            'timestamp': self.timestamp,
            'status': self.status,
            'description': HTTPStatus(self.status).phrase,
            'transaction': self.transaction,
            'exception': self.message,
            'app_name': self.app_name,
            'data': None
        }


class PageNotFound(Error):
    def __init__(self):
        context = {}
        context["status"] = 404
        context["message"] = {
            "status": 404,
            "message": "Url not found"
        }
        super(PageNotFound, self).__init__(**context)


class MethodNotAllowed(Error):
    def __init__(self):
        context = {}
        context["status"] = 405
        context["message"] = {
            "status": 405,
            "message": "Method Not Allowed"
        }
        super(MethodNotAllowed, self).__init__(**context)


class Unauthorized(Error):
    def __init__(self):
        context = {}
        context["status"] = 401
        context["message"] = {
            "status": 401,
            "message": "Unauthorized request"
        }
        super(Unauthorized, self).__init__(**context)
