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
import JYoutube
import threading
from time import sleep
import copy


class MainWindow(basewin.baseMainWindow):
    def init_main_window(self):
        self.JCDown = JYoutube.JYoutube()
        self.url = ''
        self.localDir = ''
        self.status = 5 * ['']
        self.statusBar.SetStatusWidths([90, 90, 130, 190, 100])
        self.status_thread()
        self.Stream_listCtrl.InsertColumn(0, 'No.', width=40)
        self.Stream_listCtrl.InsertColumn(1, 'Format', width=60)
        self.Stream_listCtrl.InsertColumn(2, 'Size')
        self.Stream_listCtrl.InsertColumn(3, 'Description', width=220)

    def baseMainWindowOnClose(self, event):
        self.Destroy()

    def set_format(self):
        print(self.Stream_listCtrl.GetFirstSelected())
        if self.Stream_listCtrl.GetFirstSelected() != -1:
            format_id_index = self.Stream_listCtrl.GetFirstSelected()
            format_id = self.stream_info_dict[format_id_index]['format_id']
            print('Download: ' + format_id)
            self.JCDown.set_format(format_id)
        else:
            self.JCDown.set_format('best')

    def set_proxy(self):
        if self.proxy_checkBox.GetValue():
            proxy = self.proxy_textCtrl.GetValue()
        else:
            proxy = ''
        self.JCDown.set_proxy(proxy)

    def is_individual(self):
        return self.image_save_individual_checkBox.GetValue()

    def fetch_buttonOnButtonClick(self, event):
        if not self.video_url_textCtrl.GetValue():
            self.JCDown.status[0] = 'Check'
            print('Input Check...')
        else:
            self.Stream_listCtrl.DeleteAllItems()
            self.title_staticText.SetLabel('Title: ')
            self.url = self.video_url_textCtrl.GetValue()
            self.JCDown.set_url(self.url)
            self.set_proxy()
            self.JCDown.status[0] = 'Fetch_Wait'
            self.JCDown.fetch()
            self.show_stream_list_thread()

    def download_buttonOnButtonClick(self, event):
        if not self.video_url_textCtrl.GetValue(
        ) or not self.save_local_dirPicker.Path:
            self.JCDown.status[0] = 'Check'
            print('Input Check...')
        else:
            self.url = self.video_url_textCtrl.GetValue()
            self.localDir = self.save_local_dirPicker.Path
            self.JCDown.set_url(self.url)
            self.JCDown.set_localDir(self.localDir)
            self.set_proxy()
            self.set_format()
            self.JCDown.status[0] = 'Download_Wait'
            self.JCDown.download()

    def stop_buttonOnButtonClick(self, event):
        self.JCDown.stop()

    def main_show_statusbar(self, status):
        try:
            if status[0] == 'Downloading':
                self.download_button.Enable(False)
                self.stop_button.Enable(True)
                status[0] = '下载中 -->'
            elif status[0] == 'Done':
                self.download_button.Enable(True)
                self.fetch_button.Enable(True)
                status[0] = '完成'
            elif status[0] == 'Error':
                self.download_button.Enable(True)
                self.stop_button.Enable(False)
                self.fetch_button.Enable(True)
                status[0] = '错误!'
            elif status[0] == 'Download_Wait':
                self.download_button.Enable(False)
                self.stop_button.Enable(False)
                self.fetch_button.Enable(True)
                status[0] = '即将开始下载'
            elif status[0] == 'Check':
                self.download_button.Enable(True)
                self.stop_button.Enable(False)
                self.fetch_button.Enable(True)
                status[0] = '检查输入!'
            elif status[0] == '':
                self.download_button.Enable(True)
                self.stop_button.Enable(False)
                self.fetch_button.Enable(True)
                status[0] = ''
            elif status[0] == 'Pause':
                self.download_button.Enable(True)
                self.stop_button.Enable(False)
                self.fetch_button.Enable(True)
                status[0] = '已暂停!'
            elif status[0] == 'Fetch_Wait':
                self.fetch_button.Enable(False)
                status[0] = '获取列表中~'
            elif status[0] == 'Fetch_Error':
                self.fetch_button.Enable(True)
                status[0] = '获取列表失败！'
            elif status[0] == 'Fetch_Done':
                self.fetch_button.Enable(True)
                status[0] = '获取列表成功！'
            self.statusBar.SetStatusText(status[0])
            self.statusBar.SetStatusText(status[1], 1)
            self.statusBar.SetStatusText(status[2], 2)
            self.statusBar.SetStatusText(status[3], 3)
            self.statusBar.SetStatusText(status[4], 4)
        except:
            print('App Exit!')

    def setStatus(self):
        while True:
            status = copy.deepcopy(self.JCDown.status)
            try:
                wx.CallAfter(self.main_show_statusbar, status)
                sleep(0.01)
            except:
                pass

    def status_thread(self):
        status_thread = threading.Thread(target=self.setStatus, daemon=True)
        status_thread.start()

    def main_show_stream_list(self, stream_info_dict):
        # ListCtrl显示设置
        try:
            for item in stream_info_dict:
                if item == 'title':
                    self.title_staticText.SetLabel('Title: ' +
                                                   stream_info_dict['title'])
                else:
                    self.Stream_listCtrl.InsertItem(item, str(item + 1))
                    self.Stream_listCtrl.SetItem(item, 1,
                                                 stream_info_dict[item]['ext'])
                    self.Stream_listCtrl.SetItem(
                        item, 2, stream_info_dict[item]['size'])
                    self.Stream_listCtrl.SetItem(
                        item, 3, stream_info_dict[item]['format'])
        except:
            print('Error in: show_stream_CtrlList')

    def show_stream_list(self):
        self.JCDown.ft_thread.join()
        self.stream_info_dict = copy.deepcopy(self.JCDown.stream_info_dict)
        wx.CallAfter(self.main_show_stream_list, self.stream_info_dict)
        wx.CallAfter(self.select_stream_limit_thread)

    def show_stream_list_thread(self):
        show_stream_list_thread = threading.Thread(
            target=self.show_stream_list, daemon=True)
        show_stream_list_thread.start()

    def select_stream_index(self):
        if self.Stream_listCtrl.GetFirstSelected():
            format_ID = self.Stream_listCtrl.GetFirstSelected()
            return int(format_ID)

    def _select_stream_limit(self, n):
        print('You should select ' + str(n) + ' item/items')
        while self.Stream_listCtrl.GetItemCount() and n == 1:
            # 此处为限制单个选项
            break
        while self.Stream_listCtrl.GetItemCount() and n == 2:
            # 此处为限制两个选项
            break

    def select_stream_limit_thread(self):
        print('video count: ' + str(self.Stream_listCtrl.GetItemCount()))
        if self.need_merge():
            n = 2
        else:
            n = 1
        sel_lim_thread = threading.Thread(
            target=self._select_stream_limit(n), daemon=True)
        sel_lim_thread.start()
        # while True:
        # if self.need_merge():
        # pass
        # else:
        # pass

    def Stream_listCtrlOnListItemSelected(self, event):
        format_ID = self.Stream_listCtrl.GetFirstSelected()
        print('you select: ' + str(format_ID))
        print(self.stream_info_dict[format_ID])

    def need_merge(self):
        if self.merge_VideoAndSound_checkBox.GetValue():
            return True
        else:
            return False

    def exit_menuItemOnMenuSelection(self, event):
        wx.CallAfter(self.Destroy)

    def rule_menuItemOnMenuSelection(self, event):
        # 设置对话框，网页抓取时xpath设置
        basewin.rule_Dialog(self).Show()

    def about_menuItemOnMenuSelection(self, event):
        # 关于本程序
        about_program = '''本程序用来下载：
    * YouTube以及其他国内外主流视频网站的视频

本程序基于youtube_dl开发
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
