from marshmallow import Schema, fields, validate


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
    client_id = fields.Int(
        required=True,
        load_from="client"
    )
    product_area_id = fields.Int(
        required=True,
        load_from="product_area"
    )


class ClientsSchema(Schema):
        id = fields.Int(dump_only=True)
        name = fields.Str(dump_only=True)


class ProductAreaSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)