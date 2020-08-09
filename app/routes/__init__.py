from flask import Blueprint
from ..decorators import login_required
from ..response import Response, Unauthorized
from flask import current_app as app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

book_bp = Blueprint('book', __name__, url_prefix=f'{app.config["URL_PREFIX"]}books')

@book_bp.before_request
def before_request(*args, **kwargs):
    if kwargs.get("unauthorized", False):
        return Unauthorized().to_response()
    elif kwargs.get("not_permission", False):
        return Unauthorized().to_response()

from . import book
