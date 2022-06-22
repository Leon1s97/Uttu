#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   cli.py
@Time    :   2022/06/20 09:46:01
@Author  :   Leon1s
@E-mail  :   Leon1s152427@gmail.com
@Desc    :   Start a new uttu project
"""

import sys
import os
import argparse
import cProfile
import inspect
import pkg_resources

import uttu
# from uttu.crawler import CrawlerProcess
from uttu.commands import UttuBaseCommand, UttuHelpFormatter
from uttu.exceptions import UsageError
from uttu.utils.misc import walk_modules


# sys.path.append(r"E:\Projects\Uttu")

def _iter_command_classes(module_name):
    # TODO: add `name` attribute to commands and and merge this function with
    # scrapy.utils.spider.iter_spider_classes
    for module in walk_modules(module_name):
        for obj in vars(module).values():
            if (
                    inspect.isclass(obj)
                    and issubclass(obj, UttuBaseCommand)
                    and obj.__module__ == module.__name__
                    and not obj == UttuBaseCommand
            ):
                yield obj


def _get_commands_from_module(module):
    d = {}
    for cmd in _iter_command_classes(module):
        # if inproject or not cmd.requires_project:
        #     cmdname = cmd.__module__.split(".")[-1]
        #     d[cmdname] = cmd()
        cmdname = cmd.__module__.split(".")[-1]
        d[cmdname] = cmd()
    return d


def _get_commands_from_entry_points(group="uttu.commands"):
    cmds = {}
    for entry_point in pkg_resources.iter_entry_points(group):
        obj = entry_point.load()
        if inspect.isclass(obj):
            cmds[entry_point.name] = obj()
        else:
            raise Exception(f"Invalid entry point {entry_point.name}")
    return cmds


def _get_commands_dict():
    cmds = _get_commands_from_module("uttu.commands")
    cmds.update(_get_commands_from_entry_points())
    return cmds


def _pop_command_name(argv):
    i = 0
    for arg in argv[1:]:
        if not arg.startswith("-"):
            del argv[i]
            return arg
        i += 1


def _print_header():
    version = uttu.__version__
    print(f"Uttu {version} - Next generation distributed crawler framework\n")
    print(uttu.logo)


def _print_commands():
    _print_header()
    print("Usage:")
    print("  uttu <command> [options] [args]\n")
    print("Available commands:")
    cmds = _get_commands_dict()
    for cmdname, cmdclass in sorted(cmds.items()):
        print(f"  {cmdname:<13} {cmdclass.desc()}")
    print()
    print('Use "uttu <command> -h" to see more info about a command')


def _print_unknown_command(cmdname):
    _print_header()
    print(f"Unknown command: {cmdname}\n")
    print('Use "uttu" to see available commands')


def _run_print_help(parser, func, *a, **kw):
    try:
        func(*a, **kw)
    except UsageError as e:
        if str(e):
            parser.error(str(e))
        if e.print_help:
            parser.print_help()
        sys.exit(2)


def execute(argv=None, settings=None):
    if argv is None:
        argv = sys.argv

    cmds = _get_commands_dict()
    cmdname = _pop_command_name(argv)

    if not cmdname:
        _print_commands()
        sys.exit(0)
    elif cmdname not in cmds:
        _print_unknown_command(cmdname)
        sys.exit(2)

    cmd = cmds[cmdname]
    parser = argparse.ArgumentParser(
        formatter_class=UttuHelpFormatter,
        usage=f"uttu {cmdname} {cmd.syntax()}",
        conflict_handler="resolve",
        description=cmd.desc(),
    )
    cmd.add_options(parser)
    opts, args = parser.parse_known_args(args=argv[1:])
    _run_print_help(parser, cmd.process_options, args, opts)

    cmd.crawler_process = CrawlerProcess(settings)
    _run_print_help(parser, _run_command, cmd, args, opts)
    sys.exit(cmd.exitcode)


def _run_command(cmd, args, opts):
    if opts.profile:
        _run_command_profiled(cmd, args, opts)
    else:
        cmd.run(args, opts)


def _run_command_profiled(cmd, args, opts):
    if opts.profile:
        sys.stderr.write(f"scrapy: writing cProfile stats to {opts.profile!r}\n")
    loc = locals()
    p = cProfile.Profile()
    p.runctx("cmd.run(args, opts)", globals(), loc)
    if opts.profile:
        p.dump_stats(opts.profile)


if __name__ == "__main__":
    execute(argv=["uttu", "startproject", "--name", "app", "--path", "C:/", "--templ", "sfss"])
