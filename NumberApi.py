import logging
from marshmallow import Schema, fields, ValidationError, post_dump, post_load, validates, validates_schema,EXCLUDE


class NumberApiReceiver(Schema):
    objects = fields.List(fields.Dict(required=True, error_messages={"number": "hidden"}))
    api_id = fields.Str()
    meta = fields.Dict()

    class Meta:
        exclude = ("api_id", "meta")

    def format_response_number_api(self, response):
        schema = NumberApiReceiver()
        re = schema.load(response, unknown=EXCLUDE)

    @post_load()
    def get_number_list(self, item):
        number = []
        for i in range(len(item["objects"])):
            number.append(item["objects"][i]["number"])
            logging.debug(number)
        return number




