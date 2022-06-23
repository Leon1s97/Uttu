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
from pathlib import Path, WindowsPath
from typing import Optional

import uttu
from uttu.commands import UttuBaseCommand
# from uttu.templates import render_templatefile, string_camelcase
from uttu.exceptions import UsageError, NameInvalidError, PathInvalidError

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
            return False
        else:
            return True

    @staticmethod
    def _is_valid_path(project_dir: WindowsPath):
        """
        Check project path validity
        """
        if project_dir.exists() and project_dir.is_dir():
            return True
        else:
            return False

    def add_options(self, parser):
        UttuBaseCommand.add_options(self, parser)
        parser.add_argument("-n", "--name", dest="name", required=True, help="Set project name")
        parser.add_argument("-p", "--path", dest="path", help="Set project path")
        parser.add_argument("-t", "--templ", dest="templ", choices=['sfss', 'credit'],
                            help="Using pre-built project templates")

    def _copytree(self, src, dst):
        """
        Since the original function always creates the directory, to resolve
        the issue a new function had to be created. It's a simple copy and
        was reduced for this case.

        More info at:
        https://github.com/scrapy/scrapy/pull/2005
        """
        ignore = IGNORE
        names = os.listdir(src)
        ignored_names = ignore(src, names)

        if not os.path.exists(dst):
            os.makedirs(dst)

        for name in names:
            if name in ignored_names:
                continue

            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            if os.path.isdir(srcname):
                self._copytree(srcname, dstname)
            else:
                copy2(srcname, dstname)
                _make_writable(dstname)

        copystat(src, dst)
        _make_writable(dst)

    def run(self, args, opts):
        """
        Entry point for running commands
        """
        if len(args) not in [i for i in range(0, 4)]:
            raise UsageError()

        project_name: str = opts['name']
        project_path: Optional[WindowsPath] = Path(opts['path']) if opts['path'] else None
        templ: Optional[str] = opts['templ'] if opts['templ'] else None

        if self._is_valid_name(project_name):
            self.exitcode = 1
            raise NameInvalidError()

        if self._is_valid_path(project_path):
            self.exitcode = 1
            raise PathInvalidError()

        if templ:
            # TODO: Render different project templates based on parameters[templ]
            pass
        else:
            # Render builtin project templates

            print(f"New Uttu project '{project_name}', using builtin project templates "
                  f"'{self.templates_dir}', created in:")
            print(f"    {abspath(project_dir)}\n")
            print("You can start your first spider with:")
            print(f"    cd {project_dir}")
            print("    scrapy genspider example example.com")

    @property
    def templates_dir(self):
        return Path(uttu.__path__[0]) / 'templates' / 'project'
