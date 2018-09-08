import requests
import json
import logging
from AccountDetail import AccountDetailApiReceiver
import UrlCreator


class AccountDetailApiRequester(AccountDetailApiReceiver):
    credit_value = 0

    def __init__(self):
        logging.info(AccountDetailApiReceiver.__class__.__name__ + "Initiated")

    def get_price_detail(self):
        url = UrlCreator.get_url(path=None)
        try:
            re = requests.get(url, headers=UrlCreator.headers)
            if re.status_code == 200:
                response = json.loads(re.text)
                return response
        except Exception:
            raise TimeoutError

    def set_credit_value(self):
        self.credit_value = super().format_response(self.get_price_detail())





