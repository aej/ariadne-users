from marshmallow import Schema, fields


class ErrorSchema(Schema):
    path = fields.String()
    message = fields.String()


core_types = """
    type Error {
        path: String!
        message: String!
    }
"""
