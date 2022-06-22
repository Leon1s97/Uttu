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
from twisted.python import failure
from uttu.exceptions import UsageError


class UttuBaseCommand:
    """Base class for Uttu commands"""

    def __init__(self):
        self.settings: Dict[str, Any] = {}
        self.exitcode: int = 0

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

    def add_options(self, parser):
        """
        Populate option parse with options available for this command
        """
        group = parser.add_argument_group(title='Global Options')
        group.add_argument("--logfile", metavar="FILE",
                           help="log file. if omitted stderr will be used")

    def process_options(self, args, opts):
        def arglist_to_dict(arglist):
            """Convert a list of arguments like ['arg1=val1', 'arg2=val2', ...] to a
            dict
            """
            return dict(x.split('=', 1) for x in arglist)

        try:
            self.settings.setdict(arglist_to_dict(opts.set),
                                  priority='cmdline')
        except ValueError:
            raise UsageError("Invalid -s value, use -s NAME=VALUE", print_help=False)

        if opts.logfile:
            self.settings.set('LOG_ENABLED', True, priority='cmdline')
            self.settings.set('LOG_FILE', opts.logfile, priority='cmdline')

        if opts.loglevel:
            self.settings.set('LOG_ENABLED', True, priority='cmdline')
            self.settings.set('LOG_LEVEL', opts.loglevel, priority='cmdline')

        if opts.nolog:
            self.settings.set('LOG_ENABLED', False, priority='cmdline')

        if opts.pidfile:
            with open(opts.pidfile, "w") as f:
                f.write(str(os.getpid()) + os.linesep)

        if opts.pdb:
            failure.startDebugMode()

    def run(self, args, opts):
        """
        Entry point for running commands
        """
        raise NotImplementedError


class UttuHelpFormatter(argparse.HelpFormatter):
    """
    Help Formatter for scrapy command line help messages.
    """

    def __init__(self, prog, indent_increment=2, max_help_position=24, width=None):
        super().__init__(prog, indent_increment=indent_increment,
                         max_help_position=max_help_position, width=width)

    def _join_parts(self, part_strings):
        parts = self.format_part_strings(part_strings)
        return super()._join_parts(parts)

    def format_part_strings(self, part_strings):
        """
        Underline and title case command line help message headers.
        """
        if part_strings and part_strings[0].startswith("usage: "):
            part_strings[0] = "Usage\n=====\n  " + part_strings[0][len('usage: '):]
        headings = [i for i in range(len(part_strings)) if part_strings[i].endswith(':\n')]
        for index in headings[::-1]:
            char = '-' if "Global Options" in part_strings[index] else '='
            part_strings[index] = part_strings[index][:-2].title()
            underline = ''.join(["\n", (char * len(part_strings[index])), "\n"])
            part_strings.insert(index + 1, underline)
        return part_strings
