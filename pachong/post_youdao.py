import requests
import random

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s = str(random.randint(0, 10))
    t = get_ts()
    salt=s+t
    return salt
    # print("random =", s)
    # print("ts= ", t)
    # return (print("salt =", t + s))
    # return ' 15846845789334'


def get_sign():
    return ' 9c41907df737c311c597441902ee3bc3'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
            #"1585814222752"


from_data={
    'i': '我和你都',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult':' dict',
'    client':' fanyideskweb',
'    salt': get_salt(),
'    sign': get_sign(),
'    ts': get_ts(),
'    bv':' 42160534cfa82a6884077598362bbc9d',
'    doctype':' json',
'    version':' 2.1',
'    keyfrom':' fanyi.web',
'    action':' FY_BY_REALTlME',
}

response=requests.post(url,from_data)
print(response.text)