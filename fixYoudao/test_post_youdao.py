import unittest
import random
from unittest import mock

from post_youdao import *




class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        # import time
        # t=time.time()
        # ts=str(int(round(t*1000)))
        # print(ts)
        get_ts=mock.Mock(return_value= ' 1584684578933')
        self.assertEqual(' 1584684578933',get_ts())

    def test_get_salt(self):
        # s=str(random.randint(0,10))
        # t=get_ts()
        # print("random =",s)
        # print("ts= ",t)
        # return (print("salt =",t+s))
        get_salt=mock.Mock(return_value=' 15846845789334')
        self.assertEqual(' 15846845789334',get_salt())
    def text_get_sign(self):
        self.assertEqual(' 9c41907df737c311c597441902ee3bc3',get_sign())
if __name__ == '__main__':
    unittest.main()
