import json
import requests
from flask_babel import _
from app import app
import random
from hashlib import md5
from urllib import parse


def translate(text, from_language, dest_language):
    if 'YOUDAO_TRANSLATOR_APPKEY' not in app.config or not app.config['YOUDAO_TRANSLATOR_SECRETKEY']:
        return _('Error: the translation service is not configured.')

    YOUDAO_TRANSLATOR_APPKEY = app.config['YOUDAO_TRANSLATOR_APPKEY']
    YOUDAO_TRANSLATOR_SECRETKEY = app.config['YOUDAO_TRANSLATOR_SECRETKEY']
    salt = random.randint(1, 65536)
    sign = md5((YOUDAO_TRANSLATOR_APPKEY + text + str(salt) + YOUDAO_TRANSLATOR_SECRETKEY).encode('utf-8')).hexdigest()

    response = requests.get('http://openapi.youdao.com/api?appKey={}&q={}&from={}&to={}&salt={}&sign={}'.format(
        YOUDAO_TRANSLATOR_APPKEY, parse.quote(text), from_language, dest_language, salt, sign
    ))

    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(response.content.decode('utf-8-sig'))['translation'][0]
