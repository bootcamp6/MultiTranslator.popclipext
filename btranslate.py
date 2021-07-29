# coding=utf-8

import os
import uuid
import requests
import json
from hashlib import md5
import random

class BTranslator(object):
    
    def __init__(self):
        self.APP_ID = os.environ["POPCLIP_OPTION_BAIDUAPPID"]
        self.APP_KEY = os.environ["POPCLIP_OPTION_BAIDUKEY"]
        self.API_URL = "https://fanyi-api.baidu.com/api/trans/vip/translate"

    def btranslate(self, text, bto_lang):
        """translate"""
        salt = str(random.random())
        sign = md5(self.APP_ID + text + salt + self.APP_KEY).hexdigest()
        params = {
            "q":        text,
            "from":     "auto",
            "to":       bto_lang,
            "appid":    self.APP_ID,
            "salt":     salt,
            "sign":     sign
        }

        #執行翻譯r為回覆的json
        r = requests.get(self.API_URL, params=params)
        r.encoding = 'utf-8'
        return r.json()