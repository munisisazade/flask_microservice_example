from . import book_bp
from ..models.book import Book
from ..validators.book import book_schema
from ..response import Success
from ..decorators import form_validation
from flask import request


@book_bp.route('', strict_slashes=False, methods=['GET'])
def get_all_books():
    books = Book.paginate(**request.args)
    return Success(status=200, message=books).to_response()


@book_bp.route('/<id>', methods=['GET'])
def get_book(id):
    data = Book.find_by(id=id)
    return Success(status=200, message=data).to_response()


@book_bp.route('', strict_slashes=False, methods=['POST'])
@form_validation(book_schema)
def add_book():
    data = Book(**request.json).save()
    return Success(status=201, message=data).to_response()


@book_bp.route('/<id>', methods=['PUT'])
@form_validation(book_schema)
def update_book(id):
    updated_data = Book.modify(id, **request.json)
    return Success(status=200, message=updated_data).to_response()


@book_bp.route('/<id>', methods=['DELETE'])
def delete_book(id):
    data = Book.objects(id=id).first()
    data.delete()
    return Success(status=200, message=data).to_response()
