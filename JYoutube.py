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
import copy
from copy import deepcopy
from time import sleep


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass
        print(msg)


class JYoutube(object):
    def __init__(self):
        self._running_flag = True
        self._ydl_opts = {
            'format': 'best',
            # 'format': 'best',
            # 'postprocessors': [{
            # 'key': 'FFmpegMergerPP',
            # 'preferredcodec': 'mp3',
            # 'preferredquality': '192',
            # }],
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
            'nocheckcertificate': True,
            'socket_timeout': 10,
        }
        self.status = 5 * ['']
        self.stream_list = ['']
        self.status_monitor()

    def my_hook(self, d):
        if d['status'] == 'downloading':
            if d['speed']:
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
        elif d['status'] == 'error':
            self.status[0] = 'Error'

    def set_proxy(self, proxy):
        # 设置代理，为空时清除代理
        if proxy:
            self._ydl_opts['proxy'] = proxy
        else:
            if 'proxy' in self._ydl_opts:
                self._ydl_opts.pop('proxy')

    def set_format(self, format_id):
        self._ydl_opts['format'] = format_id

    def set_url(self, url):
        self._url = url

    def set_logger(self, Logger):
        self._ydl_opts['logger'] = Logger

    def set_localDir(self, path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                os.chdir(path)
            except:
                self.status[0] = 'Error'
                self.status[1] = 'Dir Wrong!'
                print('dirmake error')
                sleep(3)
                if self.status[0] == 'Error':
                    for i in range(5):
                        self.status[i] = ''
                return
        else:
            os.chdir(path)

    def status_monitor_thread(self):
        while True:
            if self.status[0] == 'Check':
                sleep(3)
                if self.status[0] == 'Check':
                    for i in range(5):
                        self.status[i] = ''
            if self.status[0] == 'Error':
                if self.status[4] == 'Pause':
                    for i in range(1, 5):
                        self.status[i] = ''
                    self.status[0] = 'Pause'
                else:
                    sleep(3)
                    if self.status[0] == 'Error':
                        for i in range(5):
                            self.status[i] = ''
            if self.status[0] == 'Done':
                sleep(3)
                if self.status[0] == 'Done':
                    for i in range(5):
                        self.status[i] = ''
            if self.status[0] == 'Pause':
                sleep(3)
                if self.status[0] == 'Pause':
                    for i in range(5):
                        self.status[i] = ''
            if self.status[0] == 'Fetch_Error':
                sleep(3)
                if self.status[0] == 'Fetch_Error':
                    for i in range(5):
                        self.status[i] = ''
            if self.status[0] == 'Fetch_Done':
                sleep(3)
                if self.status[0] == 'Fetch_Done':
                    for i in range(5):
                        self.status[i] = ''
            sleep(0.01)

    def status_monitor(self):
        self.st_thread = threading.Thread(
            target=self.status_monitor_thread, daemon=True)
        self.st_thread.start()

    def download_thread(self):
        try:
            with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
                ydl.download([self._url])
        except:
            self.status[0] = 'Error'

    def download(self):
        self.dl_thread = threading.Thread(
            target=self.download_thread, daemon=True)
        self.dl_thread.start()

    def fetch_thread(self):
        try:
            _ydl_opts_ = {}
            _ydl_opts_ = self._ydl_opts.copy()
            # 暂时保存，后续删除
            _ydl_info_file = os.path.join(os.getcwd(), '_subtitles.txt')
            _ydl_keys_file = os.path.join(os.getcwd(), '_info_keys.txt')
            output_keys = ['title', 'ext', 'formats']
            # 以下为listbox中使用，listCtrl完成后删除
            self.stream_list = ['']
            self.stream_format_list = ['']
            # ListCtrl使用，记录格式信息
            self.stream_info_dict = {}
            stream_info_index = 0
            with youtube_dl.YoutubeDL(_ydl_opts_) as ydl_:
                print('开始获取中')
                info_dict = ydl_.extract_info(self._url, download=False)
                with open(_ydl_keys_file, 'w') as f:
                    for key in info_dict:
                        f.write(key + '\n')
                with open(_ydl_info_file, 'w') as f:
                    for out_key in output_keys:
                        f.write(out_key + ' : ' + str(info_dict[out_key]) +
                                '\n')
                self.stream_list[0] = info_dict['title']
                # ListCtrl使用
                for item in info_dict['formats'][::-1]:
                    self.stream_info_dict[stream_info_index] = {}
                    self.stream_info_dict[stream_info_index]["ext"] = item[
                        'ext']
                    try:
                        size = 'Unknown'
                        size_K = round(item['filesize'] / 1024, 2)
                        size_M = round(size_K / 1024, 2)
                        size_G = round(size_M / 1024, 2)
                        if size_G >= 1:
                            size = str(size_G) + 'GB'
                        elif size_M >= 1:
                            size = str(size_M) + 'MB'
                        else:
                            size = str(size_K) + 'KB'
                        self.stream_info_dict[stream_info_index][
                            "size"] = size
                    except:
                        self.stream_info_dict[stream_info_index]["size"] = 'Unknown'
                    self.stream_info_dict[stream_info_index]["format"] = item[
                        'format']
                    stream_info_index += 1
                self.status[0] = 'Fetch_Done'
                print('Fetch done.')
        except:
            self.status[0] = 'Fetch_Error'

    def fetch(self):
        self.ft_thread = threading.Thread(
            target=self.fetch_thread, daemon=True)
        self.ft_thread.start()

    def stop(self):
        self.terminate_thread(self.dl_thread)
        self.status[4] = 'Pause'

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
    # mydown.set_localDir('/Users/chenomg/aaa/aaaaa')
    print(mydown._ydl_opts)
    mydown.download()


if __name__ == "__main__":
    main()
