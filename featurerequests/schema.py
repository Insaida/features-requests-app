from marshmallow import Schema, fields, validate
from featurerequests.utils import check_future_date

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(dump_only=True)


class ClientsSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)


class ProductAreaSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)

class FeaturesRequestSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(
        required=True,
        validate=[validate.Length(min=6, max=255)]
    )
    description = fields.Str(required=True)
    client_priority = fields.Int(
        required=True,
        validate=[validate.Range(min=1)]
    )
    user_id = fields.Int(
        required=True,
        load_from="user"
    )
    client_id = fields.Int(
        required=True,
        load_from="client"
    )
    product_area_id = fields.Int(
        required=True,
        load_from="product_area"
    )
    user = fields.Str(dump_only=True)
    client = fields.Str(dump_only=True)
    product_area = fields.Str(dump_only=True)
    target_date = fields.Date(
        required=True,
        validate=[check_future_date],
        error_messages={
            'null': {
                'message': 'Date should be in the format YYYY-MM-DD',
                'code': 400
            },
            'validator_failed': {
                'message': 'Date should be in the format YYYY-MM-DD',
                'code': 400
            },
            'required': {
                'message': 'Target date is required in the format YYYY-MM-DD',
                'code': 400
            }
        }
    )
    created_on = fields.DateTime(dump_only=True)
    updated_on = fields.DateTime(dump_only=True)


