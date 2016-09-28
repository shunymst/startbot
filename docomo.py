#!/usr/bin/env python
# coding=utf-8
import requests
import pprint
import json

api_key = '7979414a5256614c73706c68544862777254344c58614c36575676744f48514977654e3057783963434438'


def kaiwa(kaiwa):
    json_data = {'utt':kaiwa,
                 'context':(''),
                 't': ('30')
                 }
    response = requests.post(
        #'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue',
        'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY=' + api_key,
        json.dumps(json_data),
        headers={'Content-Type': 'application/json'})
    pprint.pprint(response.json())
    resjson = response.json()

    return  resjson["utt"]

if __name__ == '__main__':
    kaiwa("こんにちは");