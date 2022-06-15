#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   sfss_spider.py
@Time    :   2022/06/09 16:22:48
@Author  :   Jianhua Ye
@Phone    :   15655140926
@E-mail :   yejh@finchina.com
@License :   (C)Copyright Financial China Information & Technology Co., Ltd.
@Desc    :   Description
@Version :   1.0
"""

# here put the import lib
from uttu.spiders import BaseSpider

class sfssSpider(BaseSpider):
    """司法诉讼爬虫框架"""
    def start_requests(self):
        # 接消息队列dataModal
        