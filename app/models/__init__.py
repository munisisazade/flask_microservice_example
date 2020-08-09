import uuid, json
from datetime import datetime
from flask_mongoengine import MongoEngine
from mongoengine import DENY
from mongoengine.fields import BaseQuerySet
from mongoengine.errors import DoesNotExist

db = MongoEngine()


class BaseModel(db.Document):
    created_at = db.DateTimeField(default=datetime.now)
    updated_at = db.DateTimeField(default=datetime.now)
    ref_map = {}
    detail_fields = []
    meta = {'allow_inheritance': True, 'abstract': True}

    @classmethod
    def single_to_dict(cls, row, fields=None):
        row_json = {'id': str(row['id'])}
        field_list = cls.detail_fields if fields else cls.only_fields
        for field in field_list:
            if field in cls.ref_map.keys():
                if field in ['service_root', 'service']:
                    name_field = 'service_name'
                else:
                    name_field = 'name'
                row_json[field + "__" + name_field] = row[field][name_field]
                row_json[field] = str(row[field]['id'])
            else:
                row_json[field] = row[field]
        return row_json

    @classmethod
    def to_formatted(cls, response_data):

        if isinstance(response_data, BaseQuerySet):
            response_json = []
            for row in response_data:
                response_json.append(cls.single_to_dict(row))
        else:
            response_json = cls.single_to_dict(response_data, cls.detail_fields)

        return response_json

    @classmethod
    def contains_fields(cls, common_fields, context):
        result = {}
        for field in common_fields:
            if '__' in field:
                value = context.pop(field)
                ref_field, search_key = field.split("__")
                try:
                    result[ref_field] = cls.ref_map[ref_field].find_by(format=False, **{search_key + "__icontains": value})
                except DoesNotExist:
                    return None
            else:
                result[field + '__icontains'] = context[field]
        return result


    @classmethod
    def paginate(cls, **kwargs):
        limit = int(kwargs.get("limit", 10))
        offset = int(kwargs.get("offset", 0))
        common_fields = set(cls.searchable_fields) & set(kwargs.keys())
        contains_query = cls.contains_fields(common_fields, kwargs)
        if contains_query is not None:
            final, count = cls.find_by(expect_unique=False, get_only_first=False, format=True, limit=limit, offset=offset,
                                       **contains_query)
        else:
            final, count = [], 0
        return {'data': final, 'rowCount': count}

    @classmethod
    def find_by(cls, limit=0, offset=10, format=True, expect_unique=True, get_only_first=True, **kwargs):
        if expect_unique:
            data = cls.objects.get(**kwargs)
        else:
            if get_only_first:
                data = cls.objects(**kwargs).first()
            else:
                data = cls.objects(**kwargs).order_by('-created_at')
                paginated = data[offset:offset+limit]
                return cls.to_formatted(paginated), len(data)
        return cls.to_formatted(data) if format else data

    @classmethod
    def modify(cls, id, **kwargs):
        updated_data = cls.objects(id=id).modify(**kwargs, new=True)
        return cls.to_formatted(updated_data)

    def save(self):
        create_data = super(BaseModel, self).save()
        return self.to_formatted(create_data)
