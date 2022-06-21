#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   exceptions.py
@Time    :   2022/06/07 11:05:32
@Author  :   Leon1s
@E-mail  :   Leon1s152427@gmail.com
@Desc    :   Exceptions in Uttu
"""


class UsageError(Exception):
    """To indicate a command-line usage error"""


class NameInvalidError(Exception):
    """To indicate a project name is invalid"""
    print('Project names must begin with a letter and contain' ' only\nletters, numbers and underscores')


class NotImplementedError(Exception):
    """To indicate a class need to be inherited"""