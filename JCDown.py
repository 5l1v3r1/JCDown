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


class MainWindow(basewin.baseMainWindow):
    def init_main_window(self, url=None):
        self.url = url

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

    def urls_input(self):
        urls_list = []
        for url in StringIO(self.URLS_textCtrl.GetValue()).readlines():
            urls_list.append(url)
        return urls_list

    def local_save_location(self):
        return self.local_dirPicker.GetPath()

    def download_buttonOnButtonClick(self, event):
        urls = self.urls_input()
        local = self.local_save_location()

    def get_large_image_links(self):
        pass

    def next_link(self):
        pass

    def rule_menuItemOnMenuSelection(self, event):
        # 设置对话框，网页抓取时xpath设置
        basewin.rule_Dialog(self).Show()

    def about_menuItemOnMenuSelection(self, event):
        # 关于本程序
        about_program = '''本程序用来下载论坛中的图片
目前支持的网站：
1. bbs.fengniao.com
2. tieba.baidu.com

后续会新增更多网站
由于这些网站调整导致图片不能下载可以通过设置配置程序修复，或者联系我
Email: xxmm@live.cn'''
        wx.MessageBox(about_program, 'About', wx.OK | wx.ICON_INFORMATION)


def main():
    app = wx.App()
    main_win = MainWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()
    # url = 'http://tieba.baidu.com/p/2166231880'
    # # 在当前目录下请先创建image文件夹
    # path = 'image'
    # crawler = Image_Downloader(url)
    # img_urls = crawler.get_image_links()
    # crawler.download_img(img_urls, path=path)


if __name__ == "__main__":
    main()
