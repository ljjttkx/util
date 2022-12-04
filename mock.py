#-*- coding: utf-8 -*-
import unittest
from unittest import mock
import requests


class Testmock(unittest.TestCase):
    def test_01(self):
        url = 'http://39.105.34.27/projects/index.php/index/user/login.html'
        data = {
            'mobile': 'cctv321',
            'password': 'as110001',
            'type': 1,
        }
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }

        response = requests.post(url=url, data=data, headers=headers).status_code
        mockdata = mock.Mock(return_value=200)
        m = mockdata(response)
        self.assertEqual(m , 300, '测试失败，返回的状态码不等于200')


if __name__ == '__main__':
    unittest.main()