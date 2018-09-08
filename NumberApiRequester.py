import requests
import json
import logging
from NumberApi import NumberApiReceiver
import UrlCreator


class NumberApiRequester(NumberApiReceiver):
    numbers = []

    def __init__(self):
        logging.info(NumberApiRequester.__class__.__name__ + "Initiated")
        super()

    def get_numbers_api(self):
        url = UrlCreator.get_url(path="Number")
        try:
            re = requests.get(url, headers=UrlCreator.headers)
            if re.status_code == 200:
                response = json.loads(re.text)
                return response
        except Exception:
            raise TimeoutError

    def set_numbers(self):
        self.numbers = super().format_response_number_api(self.get_numbers_api())
        print(self.numbers)





