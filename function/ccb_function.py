#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import os
import requests
import time
from lxml import etree
from PIL import Image
from io import BytesIO

class CCBFunction(object):

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'apply.mcard.boc.cn',
            'Origin': 'https://apply.mcard.boc.cn',
            'Referer': 'https://apply.mcard.boc.cn/apply/mobile/mainAppi/gotoIdentityVerifyPage',
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }


    def get_check_code(self):
        """
            获取验证码
        """
        self.reset_jsessionid()
        req = requests. \
            get('https://apply.mcard.boc.cn/apply/verificationCode/get?timestamp=%s' % str(round(time.time() * 1000)),
                headers=self.headers)
        b_tu = req.content
        # tu_b = base64.b64encode(b_tu)
        im = Image.open(BytesIO(b_tu))
        im.save(r'%s/tu.png' % os.getcwd(), 'PNG')
        return b_tu


    def request_check_num(self, check_code, first_name, family_name, card_num):
        """
            请求获取手机号
            check_code:验证码
            first_name: 姓
            family_name: 名字
            card_num：身份证号码
        """
        data = {
            'appiFirstName': first_name,
            'appiFamilyName': family_name,
            'appiMcIdType': '1',
            'appiMcIdNumber': card_num,
            'code': check_code,
            't': '95fbba187108880d017114e166bf13e4'
        }
        req = requests.post('https://apply.mcard.boc.cn/apply/mobile/mainAppi/getMphoneNo', data=data, headers=self.headers)
        print(req.text)


    def request_refresh_page(self):
        """
            回调获取手机号码
        """
        req = requests.get('https://apply.mcard.boc.cn/apply/mobile/mainAppi/gotoIdentityVerifyPage', headers=self.headers)
        if req.status_code == 200:
            element = etree.HTML(req.text)
            phone = element.xpath('//input[@name="appiMcMPhone"]/@value')[0]
            return phone
        else:
            print("手机号获取失败")


    def reset_jsessionid(self):
        """
            获取jsessionid并加入cookie中
        """
        req = requests.get('https://apply.mcard.boc.cn/apply/mobile/mainAppi/gotoIdentityVerifyPage')
        if req.status_code == 200:
            jsession = req.headers['Set-Cookie']
            self.headers['cookie'] = jsession
            return jsession
        else:
            print("jsessionid获取失败")

