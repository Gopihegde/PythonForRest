import requests
import json


class GET(object):
    URL = "https://api.plivo.com/v1/Account/{auth_id}/Number/"
    Auth_ID = "MAODUZYTQ0Y2FMYJBLOW"
    Auth_Token = "Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1";
    number_list = []
    uuid = ""
    sms_rate = 0
    sms_rate_price_api = 0

    credit = 0;
    headers = {
        "Authorization": "Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ==",
        "content-type": "application/json"
    }
    credit = 0

    def __init__(self, ):
        print("start")

    def get_number_api(self):
        headers = {
            "Authorization": "Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ==",
            "content-type": "application/json"
        }
        URL = 'https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Number/'
        re = requests.get(URL, headers=headers)
        if re.status_code == 200:
            output = json.loads(re.text)
            print(output)
        print(self.get_number_list(output))
        return output

    def get_number_list(self, data):
        for key, value in data.items():
            if (key == "objects"):
                for i in range(0, len(value)):
                    for k, v in value[i].items():
                        if (k == "number"):
                            self.number_list.append(v)

        return self.number_list

    def send_message_api(self):
        URL = "https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Message/"
        params = {
            "src": "14158408589",
            "dst": "14158408583",
            "text": "Hello Gopalkrishna"
        }
        re = requests.post(URL, json=params, headers=self.headers)
        if re.status_code == 202:
            output = json.loads(re.text)
        self.extract_uuid_from_json(output)

    def extract_uuid_from_json(self, output):
        for key, val in output.items():
            if (key == "message_uuid"):
                self.uuid = val[0]
        return self.uuid

    def get_message_detail(self):
        URL = "https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Message/" + self.uuid + "/"
        re = requests.get(URL, headers=self.headers)
        if (re.status_code == 200):
            output = json.loads(re.text)
            print(output)
        self.extract_price_message(output)

    def extract_price_message(self, output):
        for key, val in output.items():
            if (key == "total_rate"):
                self.sms_rate = val
                print(self.sms_rate)

    def get_price_api(self):
        URL = "https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Pricing/"
        param = {"country_iso": "US"}
        re = requests.get(URL, headers=self.headers, params=param)
        if (re.status_code == 200):
            output = json.loads(re.text)
        self.extract_price_from_api(output)

    def extract_price_from_api(self, output):
        for key, val in output.items():
            if (key == "message"):
                if (isinstance(val, dict)):
                    for k, v in val.items():
                        if (k == "outbound"):
                            self.sms_rate_price_api = v["rate"]
                            print(self.sms_rate_price_api)

    def get_account_details_api(self):
        credit = 0;
        URL = "https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/"
        re = requests.get(URL, headers=self.headers)
        print(re.text)
        if (re.status_code == 200):
            output = json.loads(re.text)
        credit = self.get_account_credit(output)
        return credit

    def get_account_credit(self, output):
        for k, v in output.items():
            if (k == "cash_credits"):
                print(type(v))
                self.credit = v
                return self.credit

    def is_proper_deduction(self, fixedrate, deductedrate):
        if (fixedrate == deductedrate):
            return True

    def is_balance_deducted(self, cred_before, cred_after):
        if (cred_before == cred_after - self.sms_rate_price_api):
            return True


if __name__ == "__main__":
    get = GET()
    # credit_after_message_sent = get.get_account_details_api()
    # credit_before_message_sent = 0
    # get.get_account_details_api()
    #get.get_number_api()
    get.send_message_api()
    get.get_message_detail()
    # get.get_price_api()
    #get.get_account_details_api()

