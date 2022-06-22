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
# import typer
from typing import Optional
from stat import S_IWUSR
from uttu.commands import UttuBaseCommand
# from uttu.templates import render_templatefile, string_camelcase
from uttu.exceptions import UsageError, NameInvalidError

_RENDER = (("${project_name}", "settings.py.tmpl"),)


def _make_writable(path):
    """Set read/write permissions"""
    current_permissions = os.stat(path).st_mode
    os.chmod(path, current_permissions | S_IWUSR)


class UttuCommand(UttuBaseCommand):
    def syntax(self):
        return "--name <project_name> --path <project_dir> --templ <template>"

    def desc(self):
        return "Start a new uttu project."

    def help(self):
        return ""

    @staticmethod
    def _is_valid_name(project_name):
        """
        Check project name validity
        """
        if not re.search(r"^[_a-zA-Z]\w*$", project_name):
            print(
                "Error: Project names must begin with a letter and contain"
                " only\nletters, numbers and underscores"
            )
        else:
            return True
        return False

    @staticmethod
    def _is_valid_path(project_dir):
        """
        Check project path validity
        """
        if not re.search(r"^[_a-zA-Z]\w*$", project_dir):
            print(
                "Error: Project names must begin with a letter and contain"
                " only\nletters, numbers and underscores"
            )
        else:
            return True
        return False

    def add_options(self, parser):
        UttuBaseCommand.add_options(self, parser)
        parser.add_argument("-n", "--name", dest="name", required=True, help="Set project name")
        parser.add_argument("-p", "--path", dest="path", help="Set project path")
        parser.add_argument("-t", "--templ", dest="templ", choices=['sfss', 'credit'],
                            help="Using pre-built project templates")

    def run(self, args, opts):
        """
        Entry point for running commands
        """
        if len(args) not in [i for i in range(0, 4)]:
            raise UsageError()


