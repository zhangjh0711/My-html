import hashlib

import requests
import random
content="我和你"
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
def get_md5(value):
    m=hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()

def get_sign():
    i=get_salt()
    e=get_content()
    s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
    # print("s=",s," md5=",get_md5(s))
    return get_md5(s)


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts
            #"1585814222752"


def get_content():
    return content


from_data={
    'i': get_content(),
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


def get_headers():
    headers={
    'cookie':'P_INFO=m15968232175@163.com|1570286779|0|other|00&99|zhj&1570286661&other#zhj&330100#10#0#0|159175&1||15968232175@163.com; _ntes_nnid=b0a2cf0dd0a4d188b7c8680102a848d8,1583404507398; OUTFOX_SEARCH_USER_ID_NCOO=1480087263.7308695; OUTFOX_SEARCH_USER_ID="-1959753667@10.169.0.82"; JSESSIONID=aaaftxvpefIuw8X7uKIfx; ___rl__test__cookies=1586501000697',
    'Referer':'http: // fanyi.youdao.com /',
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.88Safari / 537.36'
    }
    return headers





if __name__ == '__main__':
    print(from_data)
    response=requests.post(url,data=from_data,headers=get_headers())
    print(response.text)