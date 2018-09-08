import requests
import logging
import json
from SmsSender import SendMessageReceiver
from UrlCreator import get_url, headers


class SendSmsRequest(SendMessageReceiver):
    uuid = ""

    def __init__(self):
        logging.debug(SendSmsRequest.__class__.__name__)

    def send_message_request(self):
        url = get_url("Message")
        params = {
            "src": "14158408589",
            "dst": "14158408583",
            "text": "Hello ! Good Morning"
        }
        try:
            re = requests.post(url, json=params, headers=headers)
            if re.status_code == 202:
                response = json.loads(re.text)
                return response
            else:
                logging.error("Send message Failed with error" + re.status_code)

        except TimeoutError as err:
            logging.error(err)

    def get_uuid_from_message(self):
        self.uuid = super().format_sms_response(self.send_message_request())






