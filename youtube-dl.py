#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: youtube-dl.py
#          Desc: youtube-dl
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-06-07 23:29:27
#       History:
# =============================================================================
'''

import os


class YouTube_Download(object):
    def __init__(self, url):
        self.url = url
        self.proxy = ''

    def get_stream_list(self):
        stream_content = os.popen('youtube-dl' + self.proxy +
                                  ' -F --no-check-certificate ' +
                                  self.url).read()
        return stream_content.split('\n')

    def download_video(self, path=os.getcwd()):
        cmd = 'youtube-dl' + self.proxy + self.url
        info = os.popen(cmd)
        print(info.read())


def main():
    url = 'https://www.youtube.com/watch?v=bek1y2uiQGA'
    proxy = ' --proxy "socks5://127.0.0.1:1086/"  --no-check-certificate '
    format_ = ' -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" '
    myDown = YouTube_Download(url)
    myDown.proxy = proxy
    myDown.download_video()
    # print(type(myDown.get_stream_list()))
    # print(myDown.get_stream_list())


if __name__ == "__main__":
    main()
