#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2022/06/07 10:24:33
@Author  :   Leon1s
@E-mail  :   Leon1s152427@gmail.com
@Desc    :   Base class for Uttu commands
"""

import os
import argparse
from typing import Any, Dict


class BaseCommand:
    def syntax(self):
        """Command syntax (preferably one-line). Do not include command name."""
        return ""

    def desc(self):
        """A short description of the command"""
        return ""

    def help(self):
        """An extensive help for the command. It will be shown when using the
        "help" command. It can contain newlines since no post-formatting will
        be applied to its contents.
        """
        return ""
