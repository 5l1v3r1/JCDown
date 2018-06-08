#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: JYoutube.py
#          Desc:
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-06-08 23:24:30
#       History:
# =============================================================================
'''

from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'downloading':
        print(d['status'] + d['filename'] + '\t speed: ' + str(round(d['speed']/1024, 2)))
    if d['status'] == 'finished':
        print('Done downloading, now converting...')

ydl_opts = {
    'format': 'best',
    # 'postprocessors': [{
        # 'key': 'FFmpegExtractAudio',
        # 'preferredcodec': 'mp3',
        # 'preferredquality': '192',
    # }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'proxy': 'socks5://127.0.0.1:1086/',
    'nocheckcertificate': True,
}

url = 'https://www.pornhub.com/view_video.php?viewkey=ph5af4b30829920'
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
