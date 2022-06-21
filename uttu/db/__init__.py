#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/06/21 15:17:28
@Author  :   Leon1s
@E-mail  :   Leon1s152427@gmail.com
@Desc    :   Base interface for multiple databases
"""


class UttuBaseDB:
    def __init__(self, driver: str) -> None:
        self.driver = driver
    
    def conn(self):
        """Connect to the given database"""
        raise NotImplementedError
    
    