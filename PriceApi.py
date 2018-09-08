from marshmallow import fields, Schema, ValidationError, EXCLUDE, post_load
import logging


class MessageSchema(Schema):
    inbound = fields.Dict()
    outbound = fields.Dict()
    outbound_networks_list = fields.List(fields.Dict())


class PriceApiReceiver(Schema):
    api_id = fields.Str()
    country = fields.Str()
    country_code = fields.Str()
    country_iso = fields.Str()
    message = fields.Nested(MessageSchema)
    voice = fields.Dict(fields.Dict(required=True))
    tollfree = fields.Dict(fields.Dict())

    class Meta:
        exclude = ("api_id", "country", "country_code", "country_iso", "voice", "tollfree")

    @post_load()
    def get_sms_outbound_rate(self, item):
        return item["message"]["outbound"]["rate"]

    def format_price_api_response(self, response):
        schema = PriceApiReceiver()
        try:
            re = schema.load(response, unknown=EXCLUDE)
            return re
        except ValidationError as err:
            logging.error(err)
