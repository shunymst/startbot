#!/usr/bin/env python
# coding=utf-8
import requests
import pprint
import json

api_key = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'


def kaiwa(kaiwa, context):
    json_data = {'utt':kaiwa,
                 'context':context,
                 't': ('30')
                 }
    response = requests.post(
        #'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue',
        'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY=' + api_key,
        json.dumps(json_data),
        headers={'Content-Type': 'application/json'})
    pprint.pprint(response.json())
    resjson = response.json()

    # resjson["utt"]
    return resjson


if __name__ == '__main__':
    kaiwa("こんにちは", "");
