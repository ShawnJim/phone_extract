#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64

import requests
import time
from lxml import etree

from function.ccb_function import CCBFunction

if __name__ == '__main__':
    ccb = CCBFunction()
    # jsessionid = ccb.get_jsessionid()
    # print(jsessionid)
    # ccb.get_check_code(jsessionid)
    ccb.request_check_num(4, "张", "海利", "342723196808137414")
    phone = ccb.request_refresh_page()
    print(phone)
