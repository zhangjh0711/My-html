import requests
from bs4 import BeautifulSoup
url='http://www.cntour.cn/'
strhtml=requests.get(url)
# print(strhtml.text)
soup=BeautifulSoup(strhtml.text,'lxml')
date=soup.select('#main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li:nth-child(2) > a')
print(date)
for item in date:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
print(result)
# import requests
# import json
# def get_translate_date(word=None):
#     url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rul'
#     from_date={'i': '我爱中国','from': 'AUTO',' to ': ' AUTO ','smartresult': 'dict',
#     'client': 'fanyideskweb','salt': '15838054097025','sign': 'ed8c4e73754c20e41a86d42c97c6fa60',
#     'ts': '1583805409702','bv': '42160534cfa82a6884077598362bbc9d','doctype': 'json','version': '2.1',
#     'keyfrom': 'fanyi.web','action': 'FY_BY_REALTlME'}
#     response = requests.post(url,data=payload)
#     content = json.loads(response.text)
#     print(content['translateresult'][0][0]['tgt'])
# if _name_=='_main_':
#     get_translate_date('我爱数据')
