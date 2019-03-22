#coding=utf-8

'''
利用 request 请求 封装数据 DataFrame
'''

import json
import requests
from pandas import DataFrame
url='http://search.twitter.com/search.json/?q=python%20pandas'
resp = requests.get(url)
#将json数据转换成Python对象
data = json.load(resp.text)
DataFrame(data['results'],columns=['create_at','from_user','id','text'])
print(resp.text)

