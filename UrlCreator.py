headers = {
    "Authorization": "Basic TUFPRFVaWVRRMFkyRk1ZSkJMT1c6TXprME16VTFNemMzTVRjMU1URXlNR1UyTTJSbFlUSXdOMlV5TXprMQ==",
    "content-type": "application/json"
}
BaseUrl = "https://api.plivo.com/v1/Account/"
AuthId = "MAODUZYTQ0Y2FMYJBLOW"


def get_url(path):
    if path == None:
        return BaseUrl + AuthId + "/"
    else:
        return BaseUrl + AuthId + "/" + path + "/"


def get_url_message(path):
    return BaseUrl + AuthId + "/" + "Message/" + path + "/"
