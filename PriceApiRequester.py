import requests
import json
import logging
from UrlCreator import *
from PriceApi import PriceApiReceiver


class PriceApiRequester(PriceApiReceiver):
    outbound_sms_rate = 0;

    def __init__(self):
        logging.info(PriceApiRequester.__class__.__name__)

    def get_price(self):
        url = get_url("Pricing")
        param = {"country_iso": "US"}
        try:
            re = requests.get(url, headers=headers,params=param)
            if re.status_code == 200:
                res = json.loads(re.text)
                return res
        except TimeoutError as err:
            logging.error(err)

    def set_sms_rate(self):
        self.outbound_sms_rate = super().format_price_api_response(self.get_price())
        print(self.outbound_sms_rate)
        print("HI")

