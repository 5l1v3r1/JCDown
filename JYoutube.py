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
import os
import threading
from time import sleep


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class JYoutube(object):
    def __init__(self):
        self._ydl_opts = {
            'format': 'best',
            # 'postprocessors': [{
            # 'key': 'FFmpegExtractAudio',
            # 'preferredcodec': 'mp3',
            # 'preferredquality': '192',
            # }],
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
            'proxy': 'socks5://127.0.0.1:1086/',
            'nocheckcertificate': True,
        }
        self.status = 5 * ['']

    def my_hook(self, d):
        if d['status'] == 'downloading':
            if d['speed']:
                # print(d['status'] + d['filename'] + '\t speed: ' +
                      # str(round(d['speed'] / 1024, 2)))
                self.status[0] = d['status']
                self.status[1] = str(round(d['speed'] / 1024, 2)) + ' kB/s'
                if d['eta']:
                    self.status[2] = 'Remain: ' + str(
                        d['eta'] // 60) + 'min' + str(d['eta'] % 60) + 'sec'
                else:
                    self.status[2] = 'Remain: Unknown'
                self.status[3] = 'Downloaded: ' + str(
                    round(d['downloaded_bytes'] / (1024 * 1024),
                          2)) + 'MB'
        if d['status'] == 'finished':
            print('Done downloading...')
            self.status[0] = 'Done'
            sleep(3)
            self.status[0] = ''
        print(self.status)

    def set_url(self, url):
        self._url = url

    def set_localDir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)

    def download_thread(self):
        with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
            ydl.download([self._url])
        return

    def download(self):
        dl_thread = threading.Thread(target=self.download_thread, daemon=True)
        dl_thread.start()


def main():
    url = 'https://www.youtube.com/watch?v=9t2Egzzw21A'
    mydown = JYoutube()
    mydown.set_url(url)
    mydown.set_localDir('/Users/chenomg/aaa/aaaaa')
    print(mydown._ydl_opts)
    mydown.download()


if __name__ == "__main__":
    main()
