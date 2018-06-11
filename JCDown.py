#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: JCDown.py
#          Desc: download images from forum such as 蜂鸟 and 贴吧
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-06-04 08:52:42
#       History:
# =============================================================================
'''

import wx
import basewin
import requests
import re
from lxml import html
import os
from io import StringIO
import JYoutube
import threading
from time import sleep
import re


class MainWindow(basewin.baseMainWindow):
    def init_main_window(self):
        self.JCDown = JYoutube.JYoutube()
        self.url = ''
        self.localDir = ''
        self.status = 5 * ['']
        self.statusBar.SetStatusWidths([90, 90, 130, 190, 100])
        self.statusBar_thread()
        self.stop_button.Enable(False)

    def baseMainWindowOnClose(self, event):
        self.Destroy()

    def get_image_links(self):
        # 图片地址
        img_list = []
        headers = {
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        r = requests.get(self.url, headers=headers)
        selector = html.fromstring(r.text)
        for sel in selector.xpath(
                '//div[starts-with(@class, "d_post_content j_d_post_content")]'
        ):
            for img in sel.xpath("img/@src"):
                img_list.append(img)
        return img_list

    def download_img(self, img_urls, path=os.getcwd()):
        # 首先检查是否有图片
        if not img_urls:
            print('Image not found!')
        else:
            for img in img_urls:
                # 图片保存名字
                file_name = re.findall(r'\/([\d\w]+\.jpg)', img)
                if file_name:
                    # 二进制写入图片
                    with open(os.path.join(path, file_name[0]), 'wb') as f:
                        f.write(requests.get(img).content)
            print('Download done...')

    def image_urls_input(self):
        urls_list = []
        for url in StringIO(self.image_urls_textCtrl.GetValue()).readlines():
            urls_list.append(url)
        return urls_list

    def image_local_location(self):
        return self.image_local_dirPicker.GetPath()

    def image_download_buttonOnButtonClick(self, event):
        urls = self.image_urls_input()
        local = self.image_local_location()
        print(self.is_individual())

    def set_proxy(self):
        if self.proxy_checkBox.GetValue():
            proxy = self.proxy_textCtrl.GetValue()
        else:
            proxy = ''
        self.JCDown.set_proxy(proxy)

    def is_individual(self):
        return self.image_save_individual_checkBox.GetValue()

    def fetch_buttonOnButtonClick(self, event):
        pass

    def download_buttonOnButtonClick(self, event):
        if not self.video_url_textCtrl.GetValue(
        ) or not self.save_local_dirPicker.Path:
            self.JCDown.status[0] = 'check'
            print(self.JCDown.status)
            print('No URL or Path...')
        else:
            print(self.notebook.GetSelection())
            self.url = self.video_url_textCtrl.GetValue()
            self.localDir = self.save_local_dirPicker.Path
            print(self.url)
            print(self.localDir)
            self.JCDown.set_url(self.url)
            self.JCDown.set_localDir(self.localDir)
            self.set_proxy()
            self.JCDown.status[0] = 'wait'
            self.JCDown.download()
            self.download_button.Enable(False)

    def stop_buttonOnButtonClick(self, event):
        self.JCDown.stop()

    def setStatusbar(self):
        try:
            while True:
                # self.status = self.JCDown.status
                # print(self.JCDown.status)
                if self.JCDown.status[0] == 'Downloading':
                    self.download_button.Enable(False)
                    self.stop_button.Enable(True)
                    self.status = self.JCDown.status
                elif self.JCDown.status[0] == 'Done':
                    self.download_button.Enable(True)
                    self.stop_button.Enable(False)
                    self.status = self.JCDown.status
                elif self.JCDown.status[0] == 'Error':
                    self.download_button.Enable(True)
                    self.stop_button.Enable(False)
                    self.status = self.JCDown.status
                elif self.JCDown.status[0] == 'wait':
                    self.status[0] = '即将开始下载'
                elif self.JCDown.status[0] == 'check':
                    self.status[0] = 'Check Input!'
                    # print('checkcheck')
                    # if self.status[0] == 'Input Check!':
                elif self.JCDown.status[0] == '':
                    self.status[0] = ''
                self.statusBar.SetStatusText(self.status[0])
                self.statusBar.SetStatusText(self.status[1], 1)
                self.statusBar.SetStatusText(self.status[2], 2)
                self.statusBar.SetStatusText(self.status[3], 3)
                self.statusBar.SetStatusText(self.status[4], 4)
        except:
            pass

    def statusBar_thread(self):
        statusBar_thread = threading.Thread(
            target=self.setStatusbar, daemon=True)
        statusBar_thread.start()

    def get_large_image_links(self):
        pass

    def exit_menuItemOnMenuSelection(self, event):
        wx.CallAfter(self.Destroy)

    def next_link(self):
        pass

    def rule_menuItemOnMenuSelection(self, event):
        # 设置对话框，网页抓取时xpath设置
        basewin.rule_Dialog(self).Show()

    def about_menuItemOnMenuSelection(self, event):
        # 关于本程序
        about_program = '''本程序用来下载视频及图片
* 视频支持国内外主流的网站
* 图片目前支持的网站：
    1. bbs.fengniao.com
    2. tieba.baidu.com

后续会新增更多网站
由于网站调整导致不能下载可以联系我
Email: xxmm@live.cn
Created by Jase Chen'''
        wx.MessageBox(about_program, 'About', wx.OK | wx.ICON_INFORMATION)


def main():
    app = wx.App()
    main_win = MainWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
