from . import BaseModel, db, uuid


class Book(BaseModel):
    searchable_fields = ['name']
    only_fields = ['name']
    detail_fields = ['name']

    name = db.StringField(required=True, unique=True, min_length=3, max_length=200)
