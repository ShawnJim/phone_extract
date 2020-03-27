#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
from ui.main_window import MainWindowUI

if __name__ == '__main__':
        app = wx.App()
        MainWindowUI(None, title='手机号获取')
        app.MainLoop()
