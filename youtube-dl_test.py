#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: test.py
#          Desc: youtube-dl
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-06-07 18:44:24
#       History:
# =============================================================================
'''

import os
url = 'https://www.youtube.com/watch?v=bek1y2uiQGA'
id_ = "bek1y2uiQGA"
proxy = ' --proxy "socks5://127.0.0.1:1080/"'
format_ = ' -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" '
cmd = 'youtube-dl' + proxy + format_ + url
os.system(cmd)
