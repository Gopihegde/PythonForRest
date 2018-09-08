import logging
from marshmallow import fields, validates, post_load, Schema, EXCLUDE, ValidationError, pre_load


class SendMessageReceiver(Schema):
    api_id = fields.Str()
    message = fields.Str()
    message_uuid = fields.List(fields.Str(required=True))

    class Meta:
        exclude = ("api_id", "message")

    @post_load()
    def get_uuid_from_json_before_load(self, item):
        for i in range(len(item["message_uuid"])):
            return item["message_uuid"][i]

    def format_sms_response(self, response):
        schema = SendMessageReceiver()
        try:
            res = schema.load(response,unknown=EXCLUDE)
            return res
        except ValidationError as err:
            logging.error(err)
