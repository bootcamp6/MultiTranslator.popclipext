import uuid
import requests
import os

class Translator(object):

    def __init__(self):
        self.key = os.environ["POPCLIP_OPTION_MSKEY"]

    def translate(self, text, to_lang):

        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/translate?api-version=3.0'
        params = '&to=' + to_lang
        constructed_url = base_url + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': text
        }]

        request = requests.post(constructed_url, headers=headers, json=body)

        if request.status_code == requests.codes.ok:
            request.encoding = 'utf-8'
            return request.json()
        else:
            raise Exception('Failed to obtain translation')
