import logging
from marshmallow import Schema, fields, ValidationError, post_dump, post_load, validates, validates_schema


class AccountDetailApiReceiver(Schema):
    account_type = fields.Str()
    address = fields.Str()
    api_id = fields.Str()
    auth_id = fields.Str()
    auto_recharge = fields.Boolean()
    billing_mode = fields.Str()
    cash_credits = fields.Str(required=True, error_messages={"cash_credits": "field required"})
    city = fields.Str()
    name = fields.Str()
    resource_uri = fields.Str()
    state = fields.Str()
    timezone = fields.Str()

    @post_load()
    def get_credit_info(self, item):
        try:
            for key, value in item.items():
                if key == "cash_credits":
                    logging.debug("cash credit is" + "" + value)
                    return value
        except AttributeError as err:
            logging.error(err)
        finally:
            logging.info("Executed")

    def format_response(self, response):
        schema = AccountDetailApiReceiver()
        try:
            res = schema.load(response)
            return res
        except ValidationError as error:
            logging.error(error.messages)
            logging.info("Valid is" + error.valid_data)


