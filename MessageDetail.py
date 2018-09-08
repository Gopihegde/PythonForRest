import logging
from marshmallow import fields, EXCLUDE, post_load, ValidationError, Schema


class MessageDetailReceiver(Schema):
    api_id = fields.Str()
    error_code = fields.Str()
    from_number = fields.Str()
    message_direction = fields.Str()
    message_state = fields.Str()
    message_time = fields.DateTime()
    message_type = fields.Str()
    message_uuid = fields.Str()
    resource_uri = fields.Str()
    to_number = fields.Int()
    total_amount = fields.Int()
    total_rate = fields.Float()
    units = fields.Int()

    class Meta:
        exclude = (
            "api_id", "error_code", "from_number", "message_direction", "message_state", "message_time", "message_type",
            "message_uuid", "resource_uri", "to_number", "total_amount", "units")

    @post_load()
    def get_detail_from_uuid(self, item):
        return item["total_rate"]

    def get_message_detail(self, response):
        schema = MessageDetailReceiver()
        try:
            re = schema.load(response, unknown=EXCLUDE)
            return re
        except ValidationError as err:
            logging.error(err)
