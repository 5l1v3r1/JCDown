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
import ctypes
from time import sleep


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass
        # print(msg)


class JYoutube(object):
    def __init__(self):
        self._running_flag = True
        self._ydl_opts = {
            'format': 'best',
            # 'postprocessors': [{
            # 'key': 'FFmpegExtractAudio',
            # 'preferredcodec': 'mp3',
            # 'preferredquality': '192',
            # }],
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
            'nocheckcertificate': True,
            'socket_timeout': 10
        }
        self.status = 5 * ['']

    def my_hook(self, d):
        if d['status'] == 'downloading':
            if d['speed']:
                # print(d['status'] + d['filename'] + '\t speed: ' +
                # str(round(d['speed'] / 1024, 2)))
                self.status[0] = 'Downloading'
                self.status[1] = str(round(d['speed'] / 1024, 2)) + ' kB/s'
                if d['eta']:
                    self.status[2] = 'Remain: ' + str(
                        d['eta'] // 60) + 'min' + str(d['eta'] % 60) + 'sec'
                else:
                    self.status[2] = 'Remain: Unknown'
                self.status[3] = 'Downloaded: ' + str(
                    round(d['downloaded_bytes'] / (1024 * 1024), 2)) + 'MB'
        elif d['status'] == 'finished':
            print('Done downloading...')
            self.status[0] = 'Done'
            sleep(3)
            if self.status[0] == 'Done':
                self.status[0] = ''
        elif d['status'] == 'error':
            print('Error')
            self.status[0] = 'Error'
            sleep(3)
            if self.status[0] == 'Error':
                self.status[0] = ''

    def set_proxy(self, proxy):
        self._ydl_opts['proxy'] = proxy

    def set_url(self, url):
        self._url = url

    def set_logger(self, Logger):
        self._ydl_opts['logger'] = Logger

    def set_localDir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)

    def download_thread(self):
        try:
            with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
                ydl.download([self._url])
        except:
            self.status[0] = 'Error'
            sleep(3)
            if self.status[0] == 'Error':
                self.status[0] = ''

    def download(self):
        self.dl_thread = threading.Thread(target=self.download_thread, daemon=True)
        self.dl_thread.start()

    def stop(self):
        self.terminate_thread(self.dl_thread)

    def terminate_thread(self, thread):
        # 由于youtube_dl一旦运行无法停止，所以停止下载的话只能强制停止该线程
        if not thread.isAlive():
            return
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread.ident), exc)
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

def main():
    url = 'https://www.youtube.com/watch?v=9t2Egzzw21A'
    mydown = JYoutube()
    mydown.set_url(url)
    mydown.set_localDir('/Users/chenomg/aaa/aaaaa')
    print(mydown._ydl_opts)
    mydown.download()


if __name__ == "__main__":
    main()
