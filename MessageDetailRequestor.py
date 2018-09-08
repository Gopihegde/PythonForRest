import requests
import json
import logging
from MessageDetail import MessageDetailReceiver
from UrlCreator import *
from SmsRequester import SendSmsRequest


class MessageDetailApiRequester(MessageDetailReceiver, SendSmsRequest):
    sms_rate = 0
   # uuid = ""

    def __init__(self):
        logging.info(MessageDetailApiRequester.__class__.__name__)

    def send_sms(self):
        super().get_uuid_from_message()


    def get_message_detail_api(self):
        url = get_url_message(self.uuid)
        try:
            re = requests.get(url, headers=headers)
            res = json.loads(re.text)
            return res
        except TimeoutError as err:
            logging.error(err)

    def set_sms_rate(self):
        self.sms_rate = super().get_message_detail(self.get_message_detail_api())
        


if __name__ == '__main__':
    test = MessageDetailApiRequester()
    test.send_sms()
    test.set_sms_rate()
