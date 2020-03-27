# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 载入必要的模块
import wx
import os
import pygame
from pygame.locals import *
import itertools
import random
import base64
from PIL import Image
from io import BytesIO
from function.ccb_function import CCBFunction

class Example(wx.Frame):


    def __init__(self, parent, title):
        self.CCBFunction = CCBFunction()
        #继承父类wx.Frame的初始化方法，并设置窗口大小为620*420
        super(Example, self).__init__(parent, title = title, size=(620, 420))
        self.InitUI()
        self.Centre()
        self.Show()


    def InitUI(self):
        # 产生验证码图片
        self.CCBFunction.get_check_code()

        # 利用wxpython的GridBagSizer()进行页面布局
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(10, 5) #列间隔为10，行间隔为5

        # 添加姓字段，并加入页面布局，为第一行，第一列
        first_name = wx.StaticText(panel, label="姓")
        sizer.Add(first_name, pos = (0, 0), flag=wx.ALL, border=5)

        # 添加文本框字段，并加入页面布局，为第一行，第2列
        self.first_name_input = wx.TextCtrl(panel)
        sizer.Add(self.first_name_input, pos=(0, 1), flag=wx.ALL, border=5)

        # 添加名字段，并加入页面布局，为第一行，第3列
        family_name = wx.StaticText(panel, label="名", )
        sizer.Add(family_name, pos=(0, 2), flag=wx.ALL, border=5)

        # 添加文本框字段，以星号掩盖,并加入页面布局，为第1行，第4列
        self.family_name_input = wx.TextCtrl(panel)
        sizer.Add(self.family_name_input, pos=(0, 3), flag=wx.ALL, border=5)

        # 添加身份证号字段，并加入页面布局，为第一行，第3列
        card_mum = wx.StaticText(panel, label="身份证")
        sizer.Add(card_mum, pos=(1, 0),flag=wx.ALL, border=5)

        # 添加文本框字段，以星号掩盖,并加入页面布局，为第1行，第4列
        self.card_num_input = wx.TextCtrl(panel, size=(200, 25))
        sizer.Add(self.card_num_input, pos=(1, 1), span=(1, 2), flag=wx.ALL, border=7)

        # 添加验证码字段，并加入页面布局，为第三行，第一列
        check_code = wx.StaticText(panel, label="验证码")
        sizer.Add(check_code, pos=(2, 0), flag=wx.ALL, border=5)

        # 添加文本框字段，并加入页面布局，为第三行，第2列
        self.check_code_input = wx.TextCtrl(panel)
        sizer.Add(self.check_code_input, pos=(2, 1), flag=wx.ALL, border=5)

        # 添加验证码图片，并加入页面布局，为第三行，第3列
        image = wx.Image(r'%s/tu.png' % os.getcwd(), wx.BITMAP_TYPE_PNG).Rescale(80,25).ConvertToBitmap()  # 获取图片，转化为Bitmap形式
        self.bmp= wx.StaticBitmap(panel, -1, image) #转化为wx.StaticBitmap()形式
        sizer.Add(self.bmp, pos=(2, 2), flag=wx.ALL, border=5)

        # 添加登录按钮，并加入页面布局，为第四行，第2列
        btn = wx.Button(panel, -1, "提交")
        sizer.Add(btn, pos=(3, 1), flag=wx.ALL, border=5)

        # 添加验证码字段，并加入页面布局，为第三行，第一列
        phone = wx.StaticText(panel, label="获取手机号")
        sizer.Add(phone, pos=(4, 0), flag=wx.ALL, border=5)

        # 添加文本框字段，并加入页面布局，为第三行，第2列
        self.phone_num_input = wx.TextCtrl(panel)
        sizer.Add(self.phone_num_input, pos=(4, 1), flag=wx.ALL, border=5)

        # 为登录按钮绑定login_process事件
        self.Bind(wx.EVT_BUTTON, self.get_phone_num, btn)
        # 将Panmel适应GridBagSizer()放置
        panel.SetSizerAndFit(sizer)

    # 事件处理
    def get_phone_num(self, event):
        first_name = self.first_name_input.GetValue()
        family_name = self.family_name_input.GetValue()
        card_num = self.card_num_input.GetValue()
        check_code = self.check_code_input.GetValue()
        self.CCBFunction.request_check_num(check_code=check_code, first_name=first_name, family_name=family_name, card_num=card_num)
        phone = self.CCBFunction.request_refresh_page()
        if phone:
            self.phone_num_input.SetValue(phone)
        else:
            return
        # 刷新验证码
        self.CCBFunction.get_check_code()
        image = wx.Image(r'%s/tu.png' % os.getcwd(), wx.BITMAP_TYPE_PNG).Rescale(80,25).ConvertToBitmap()
        self.bmp.SetBitmap(wx.BitmapFromImage(image))



#主函数
def main():
    app = wx.App()
    Example(None, title = '手机号获取')
    app.MainLoop()

main()