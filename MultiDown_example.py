#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: example.py
#          Desc: 多任务下载示例
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-07-01 23:09:02
#       History:
# =============================================================================
'''
from video_dl import MultiDown
from lxml import html
import requests
from time import sleep


class Extract_Video_URLs(object):
    """
    提取网址列表
    """
    def __init__(self):
        self._headers = {
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        self._proxies = {
            "http": "socks5://127.0.0.1:1080",
            "https": "socks5://127.0.0.1:1080",
        }

    def get_url_list(self, url):
        # 获取网址列表
        url_list = []
        response = requests.get(
            url, headers=self._headers, proxies=self._proxies)
        print('response.status_code: ' + str(response.status_code))
        print('response.encoding: ' + str(response.encoding))
        # 网页转换为lxml可用
        tree = html.fromstring(response.text)
        for url in tree.xpath('//div[@class="wrap"]/div/div/a/@href'):
            url_list.append('https://www.example.com' + url)
        for item in url_list:
            print(item)
        return url_list

def main():
    url = 'https://www.example.com'
    URLS = Extract_Video_URLs()
    url_list = URLS.get_url_list(url)
    print('Length of list: {}'.format(len(url_list)))
    Worker = MultiDown()
    Worker.init_url_list(url_list, 8)
    Worker.set_localDir('/Volumes/40G/video')
    Worker.working()

if __name__ == "__main__":
    main()
