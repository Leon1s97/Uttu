#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   startproject.py
@Time    :   2022/06/07 10:40:01
@Author  :   Leon1s
@E-mail  :   Leon1s152427@gmail.com
@Desc    :   Start a new uttu project
"""
import os
import re
from stat import S_IWUSR
from uttu.commands import BaseCommand
from scrapy.exceptions import UsageError, NameInvalidError

_RENDER = (
    ('${project_name}', 'settings.py.tmpl'),
)


def _make_writable(path):
    """Set read/write permissions"""
    current_permissions = os.stat(path).st_mode
    os.chmod(path, current_permissions | S_IWUSR)


class UttuCommand(BaseCommand):
    def syntax(self):
        return "<project_name> [project_dir]"

    def desc(self):
        return "Start a new uttu project."

    def _is_valid_name(self, project_name):
        if not re.search(r'^[_a-zA-Z]\w*$', project_name):
            print('Error: Project names must begin with a letter and contain'
                  ' only\nletters, numbers and underscores')
        else:
            return True
        return False