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
        self.pick_best_format()
        self._ydl_opts = {
            'format': self._format,
            'logger': MyLogger(),
            'progress_hooks': [self.my_hook],
            'nocheckcertificate': True,
            'socket_timeout': 10,
        }
        self.status = 5 * ['']

    def pick_best_format(self):
        def is_Exit_ffmpeg():
            flag = os.system('ffmpeg -version')
            if flag== 0:
                return True
            else:
                return False
        if is_Exit_ffmpeg():
            self._format = 'bestvideo+bestaudio'
        else:
            self._format = 'best'

    def my_hook(self, d):
        # 下载状态保存到self.status
        if d['status'] == 'downloading':
            if d['speed']:
                self.status[0] = 'Downloading'
                speed_k = round(d['speed'] / 1024, 2)
                speed_m = round(speed_k / 1024, 2)
                speed_g = round(speed_m / 1024, 2)
                if speed_g >= 1:
                    speed = str(speed_g) + ' GB/s'
                elif speed_m >= 1:
                    speed = str(speed_m) + ' MB/s'
                else:
                    speed = str(speed_k) + ' KB/s'
                # 实时下载速度
                self.status[1] = speed
                remain_s = d['eta']
                remain_m = remain_s // 60
                remain_h = remain_m // 60
                remain_d = remain_h // 24
                if remain_d >= 1:
                    self.status[2] = 'Remain: ' + '> 1day'
                elif remain_h >= 1:
                    self.status[2] = 'Remain: ' + str(remain_h) + 'h' + str(
                        round(remain_m % 60)) + 'm' + str(
                            round(remain_s % 60)) + 's'
                elif remain_m >= 1:
                    self.status[2] = 'Remain: ' + str(remain_m) + 'm' + str(
                        round(remain_s % 60)) + 's'
                else:
                    self.status[2] = 'Remain: ' + str(remain_s) + 's'
                down_size_k = round(d['downloaded_bytes'] / 1024, 2)
                down_size_m = round(down_size_k / 1024, 2)
                down_size_g = round(down_size_m / 1024, 2)
                if down_size_g >= 1:
                    down_size = str(down_size_g) + 'GB'
                elif down_size_m >= 1:
                    down_size = str(down_size_m) + 'MB'
                else:
                    down_size = str(down_size_k) + 'KB'
                self.status[3] = 'Downloaded: ' + down_size
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

    def download_thread(self):
        try:
            with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
                ydl.download([self._url])
        except:
            self.set_format('best')
            print('预选最佳合并方案出错，改用best')
            try:
                with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
                    ydl.download([self._url])
            except:
                self.status[0] = 'Error'
                print('Download Error')

    def download(self):
        self.dl_thread = threading.Thread(target=self.download_thread)
        self.dl_thread.start()

    def fetch_thread(self):
        # 视频信息保存到self.stream_info_dict
        try:
            _ydl_opts_ = {}
            _ydl_opts_ = self._ydl_opts.copy()
            # 暂时保存，后续删除
            _ydl_info_file = os.path.join(os.getcwd(), '_subtitles.txt')
            _ydl_keys_file = os.path.join(os.getcwd(), '_info_keys.txt')
            output_keys = ['title', 'ext', 'formats']
            # ListCtrl使用，记录格式信息
            self.stream_info_dict = {}
            stream_info_index = 0
            with youtube_dl.YoutubeDL(_ydl_opts_) as ydl_:
                print('开始获取中')
                info_dict = ydl_.extract_info(self._url, download=False)
                # 输出获取的视频信息保存到文本文件中
                # with open(_ydl_keys_file, 'w') as f:
                # for key in info_dict:
                # f.write(key + ':' + str(info_dict[key]) + '\n')
                # with open(_ydl_info_file, 'w') as f:
                # for out_key in output_keys:
                # f.write(out_key + ' : ' + str(info_dict[out_key]) +
                # '\n')
                self.stream_info_dict['title'] = info_dict['title']
                # ListCtrl使用
                for item in info_dict['formats'][::-1]:
                    self.stream_info_dict[stream_info_index] = {}
                    self.stream_info_dict[stream_info_index]["ext"] = item[
                        'ext']
                    try:
                        size = '-'
                        size_K = round(item['filesize'] / 1024, 2)
                        size_M = round(size_K / 1024, 2)
                        size_G = round(size_M / 1024, 2)
                        if size_G >= 1:
                            size = str(size_G) + 'GB'
                        elif size_M >= 1:
                            size = str(size_M) + 'MB'
                        else:
                            size = str(size_K) + 'KB'
                        self.stream_info_dict[stream_info_index]["size"] = size
                    except:
                        self.stream_info_dict[stream_info_index]["size"] = '-'
                    self.stream_info_dict[stream_info_index]["format"] = item[
                        'format']
                    self.stream_info_dict[stream_info_index][
                        "format_id"] = item['format_id']
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
        self.status[4] = ' '

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


class Multi_Down(object):
    def __init__(self):
        # 总的线程列表
        self._thread_list = []
        # 目前正在运行的线程数量
        self._threading_count = 0
        # 待运行的线程编号
        self._threading_index = 0
        self._localDir = os.path.join(os.getcwd(), 'video')

    def init_url_list(self, url_list, count=1):
        self._count = count
        self._url_list = url_list

    def _working_thread(self):
        while True:
            while self._threading_count < self._count:
                if self._threading_index == len(self._thread_list):
                    break
                self._thread_list[self._threading_index].download()
                print('Thread{} generated!'.format(self._threading_index))
                self._threading_index += 1
                self._threading_count += 1
                print('Thread running: {}'.format(self._threading_count))
            for i in range(self._threading_index):
                if self._thread_list[i].status[0] == 'Done':
                    print('                     Thread{} done!'.format(i))
                    self._thread_list[i].status[0] = ''
                    self._threading_count -= 1
                    print('Thread running: {}'.format(self._threading_count))
                if self._thread_list[i].status[0] == 'Error':
                    print(
                        '                                     Thread{} Error!'.
                        format(i))
                    self._thread_list[i].status[0] = ''
                    self._threading_count -= 1
                    print('Thread running: {}'.format(self._threading_count))
            if self._threading_index == len(self._thread_list):
                break

    def working(self):
        self.gene_threads()
        working_thread = threading.Thread(target=self._working_thread)
        working_thread.start()

    def set_localDir(self, localDir):
        if localDir:
            self._localDir = localDir

    def gene_threads(self):
        if len(self._url_list) > len(self._thread_list):
            for url in self._url_list[len(self._thread_list)::]:
                index = len(self._thread_list)
                self._thread_list.append('')
                self._thread_list[index] = JYoutube()
                self._thread_list[index].set_proxy("socks5://127.0.0.1:1080/")
                self._thread_list[index].set_url(url)
                self._thread_list[index].set_localDir(self._localDir)

    def add_url(self, url):
        if url:
            self._url_list.append(url)
            self.gene_threads()


def main():
    total_list = [
        'https://www.youtube.com/watch?v=jzbiRNaj_v0',
        'https://www.youtube.com/watch?v=ui4jqQV7rco',
        'https://www.youtube.com/watch?v=Nz-dPOjK1gQ',
        'https://www.youtube.com/watch?v=r-AuLm7S3XE',
    ]
    Worker = Multi_Down()
    Worker.init_url_list(total_list, 4)
    Worker.set_localDir('/Volumes/40G/video')
    Worker.working()
    addd = [
        'https://www.youtube.com/watch?v=PLDIhqMWH00',
        'https://www.youtube.com/watch?v=EqREabQUALE',
        'https://www.youtube.com/watch?v=AtKZKl7Bgu0',
        'https://www.youtube.com/watch?v=0caYeLf-Lc4',
        'https://www.youtube.com/watch?v=Exdt3upYpqA',
        'https://www.youtube.com/watch?v=coYCDufkfPM',
    ]
    for url in addd:
        Worker.add_url(url)


if __name__ == "__main__":
    main()
