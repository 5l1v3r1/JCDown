#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: JCDown.py
#          Desc: GUI: download videos from YouTube and other sites
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-07-01 22:51:16
#       History:
# =============================================================================
'''

import wx
import basewin
import video_dl
import threading
from time import sleep
import copy


class MainWindow(basewin.baseMainWindow):
    """
    GUI应用，用于下载YouTube及其他支持的视频网站视频下载
    """

    def init_main_window(self):
        # 实例化单视频下载模块
        self.JCDown = video_dl.VideoDownload()
        # 下载视频网址
        self.url = ''
        # 本地保存地址
        self.localDir = ''
        # 从video_dl复制并保存下载状态
        self.status = 5 * ['']
        # 状态栏分块
        self.statusBar.SetStatusWidths([110, 130, 120, 170, 100])
        # 定时获取下载状态值并发送给主线程设置状态栏
        self.status_thread()
        # 状态值经过三秒后重置
        self.status_reset()
        # 获取视频信息列表显示列名
        self.Stream_listCtrl.InsertColumn(0, 'No.', width=40)
        self.Stream_listCtrl.InsertColumn(1, 'Format', width=60)
        self.Stream_listCtrl.InsertColumn(2, 'Size')
        self.Stream_listCtrl.InsertColumn(3, 'Description', width=220)

    def baseMainWindowOnClose(self, event):
        """
        点击窗口关闭
        """
        self.Destroy()

    def select_count_check(self):
        """
        返回视频选择数量
        """
        if self.Stream_listCtrl.GetSelectedItemCount() == 2:
            return 2
        elif self.Stream_listCtrl.GetSelectedItemCount() == 1:
            return 1
        elif self.Stream_listCtrl.GetSelectedItemCount() == 0:
            return 0
        else:
            print('选项过多')
            return -1

    def set_format(self):
        """
        设置下载格式
        """
        if self.select_count_check() == 2:
            # 若选择两项则使用合并视频和音频
            format_id_index1 = self.Stream_listCtrl.GetFirstSelected()
            format_id_index2 = self.Stream_listCtrl.GetNextSelected(
                format_id_index1)
            format_id1 = self.stream_info_dict[format_id_index1]['format_id']
            format_id2 = self.stream_info_dict[format_id_index2]['format_id']
            print('Download: ' + format_id1 + '+' + format_id2)
            self.JCDown.set_format(format_id1 + '+' + format_id2)
        elif self.select_count_check() == 1:
            format_id_index = self.Stream_listCtrl.GetFirstSelected()
            format_id = self.stream_info_dict[format_id_index]['format_id']
            print('Download: ' + format_id)
            self.JCDown.set_format(format_id)
        else:
            # 未选时自动使用最佳画质格式
            self.JCDown.pick_best_format()

    def set_proxy(self):
        """
        设置代理proxy
        """
        if self.proxy_checkBox.GetValue():
            proxy = self.proxy_textCtrl.GetValue()
        else:
            proxy = ''
        self.JCDown.set_proxy(proxy)

    def fetch_buttonOnButtonClick(self, event):
        """
        获取按钮事件
        """
        if not self.video_url_textCtrl.GetValue():
            self.JCDown.status[0] = 'Check'
            print('Input Check...')
        else:
            # 清空标题和列表栏
            self.title_textCtrl.SetValue('')
            self.Stream_listCtrl.DeleteAllItems()
            # 设置获取参数
            self.url = self.video_url_textCtrl.GetValue()
            self.JCDown.set_url(self.url)
            self.set_proxy()
            self.JCDown.status[0] = 'Fetch_Wait'
            self.JCDown.fetch()
            self.show_stream_list_thread()

    def download_buttonOnButtonClick(self, event):
        """
        下载按钮事件
        """
        if not self.video_url_textCtrl.GetValue(
        ) or not self.save_local_dirPicker.Path or self.select_count_check(
        ) == -1:
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
        """
        暂停按钮事件
        """
        self.JCDown.stop()

    def main_show_statusbar(self, status):
        """
        显示应用状态栏信息
        """
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
            elif status[0] == 'Select_One':
                status[0] = '已选一项！'
            elif status[0] == 'Select_Two':
                status[0] = '已选两项！'
            elif status[0] == 'Select_Error':
                status[0] = '请检查选择项！'
            self.statusBar.SetStatusText(status[0])
            self.statusBar.SetStatusText(status[1], 1)
            self.statusBar.SetStatusText(status[2], 2)
            self.statusBar.SetStatusText(status[3], 3)
            self.statusBar.SetStatusText(status[4], 4)
        except:
            # 程序退出后无法设置状态栏
            print('App Exit!')

    def setStatus(self):
        """
        获取下载状态并传送到主线程显示
        """
        while True:
            status = copy.deepcopy(self.JCDown.status)
            try:
                wx.CallAfter(self.main_show_statusbar, status)
                sleep(0.01)
            except:
                pass

    def status_thread(self):
        """
        用于显示状态栏线程(获取下载状态并传送到主线程显示)
        """
        status_thread = threading.Thread(target=self.setStatus, daemon=True)
        status_thread.start()

    def status_reset_thread(self):
        """
        重置下载状态值
        """
        while True:
            if self.JCDown.status[0] == 'Check':
                sleep(3)
                if self.JCDown.status[0] == 'Check':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            if self.JCDown.status[0] == 'Error':
                if self.JCDown.status[4] == ' ':
                    pass
                else:
                    sleep(3)
                    if self.JCDown.status[0] == 'Error':
                        for i in range(5):
                            self.JCDown.status[i] = ''
            if self.JCDown.status[4] == ' ':
                for i in range(1, 5):
                    self.JCDown.status[i] = ''
                self.JCDown.status[0] = 'Pause'
            if self.JCDown.status[0] == 'Done':
                sleep(3)
                if self.JCDown.status[0] == 'Done':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            if self.JCDown.status[0] == 'Pause':
                sleep(3)
                if self.JCDown.status[0] == 'Pause':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            if self.JCDown.status[0] == 'Fetch_Error':
                sleep(3)
                if self.JCDown.status[0] == 'Fetch_Error':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            if self.JCDown.status[0] == 'Fetch_Done':
                sleep(3)
                if self.JCDown.status[0] == 'Fetch_Done':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            if self.JCDown.status[0] == 'Select_One':
                sleep(3)
                if self.JCDown.status[0] == 'Select_One':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            if self.JCDown.status[0] == 'Select_Two':
                sleep(3)
                if self.JCDown.status[0] == 'Select_Two':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            if self.JCDown.status[0] == 'Select_Error':
                sleep(3)
                if self.JCDown.status[0] == 'Select_Error':
                    for i in range(5):
                        self.JCDown.status[i] = ''
            sleep(0.01)

    def status_reset(self):
        self.st_thread = threading.Thread(
            target=self.status_reset_thread, daemon=True)
        self.st_thread.start()

    def main_show_stream_list(self, stream_info_dict):
        # ListCtrl显示设置
        try:
            for item in stream_info_dict:
                if item == 'title':
                    self.title_textCtrl.SetValue(stream_info_dict['title'])
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
        # 等待获取视频信息线程结束
        self.JCDown.ft_thread.join()
        self.stream_info_dict = copy.deepcopy(self.JCDown.stream_info_dict)
        # 将信息传递到主线程显示
        wx.CallAfter(self.main_show_stream_list, self.stream_info_dict)

    def show_stream_list_thread(self):
        show_stream_list_thread = threading.Thread(
            target=self.show_stream_list, daemon=True)
        show_stream_list_thread.start()

    def select_stream_index(self):
        if self.Stream_listCtrl.GetFirstSelected():
            format_ID = self.Stream_listCtrl.GetFirstSelected()
            # 返回视频选择序号
            return int(format_ID)

    def Stream_listCtrlOnListItemSelected(self, event):
        """
        点击视频列表事件
        """
        format_ID = self.Stream_listCtrl.GetFirstSelected()
        count = self.Stream_listCtrl.GetSelectedItemCount()
        if count == 1:
            self.JCDown.status[0] = 'Select_One'
        elif count == 2:
            self.JCDown.status[0] = 'Select_Two'
        else:
            self.JCDown.status[0] = 'Select_Error'
        print('you select: ' + str(format_ID))
        print(self.stream_info_dict[format_ID])

    def exit_menuItemOnMenuSelection(self, event):
        """
        点击菜单栏退出事件
        """
        wx.CallAfter(self.Destroy)

    def rule_menuItemOnMenuSelection(self, event):
        # 设置对话框
        basewin.rule_Dialog(self).Show()

    def about_menuItemOnMenuSelection(self, event):
        # 关于本程序
        about_program = '''本程序用来下载：
    * YouTube以及其他国内外主流视频网站的视频

本程序基于youtube_dl开发
GitHub: https://github.com/chenomg/JCDown
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
