import json
import random
import requests
import time


# url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# content="我和你"

class Youdao():
    def __init__(self, content):
        self.content = content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_salt(self):
        s = str(random.randint(0, 10))
        t = self.ts

        # print("random = ",s)
        # print("ts= ",t)
        # print("salt= ",t+s)
        return t + s
        # return '15846848803956'

    def get_md5(self, value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i = self.salt
        e = self.content
        s = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        # print("s=",s,"  md5=",get_md5(s))
        return self.get_md5(s)
        # return '1537e6e7d4296b0145432358da1fce0'

    def get_ts(self):
        t = time.time()
        ts = str(int(round(t * 1000)))

        return ts
        # '1585615400595'

    # def get_content(self):
    #     return content

    def yield_form_data(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '9ef61dc3d2f65f61d71a16bd47c6e9ee',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_data

    def get_headers(self):
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-715101748@10.108.160.17; JSESSIONID=aaam7kNNEvn887axRKIfx; OUTFOX_SEARCH_USER_ID_NCOO=1372491966.423369; ___rl__test__cookies=1586496832856',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }
        return headers

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        content = json.loads(response.text)
        return content['translateResult'][0][0]['tgt']


if __name__ == '__main__':
   while(True):
       try:
            i=input("please input  :")
            youdao=Youdao(i)
            print("fanyi result :",youdao.fanyi())
       except:
            pass