#! /usr/bin/env python3
import os
import click

from . import util, tool_lib as lib


def get_env_vars(ctx, args, incomplete):
    return [k for k in os.environ.keys() if incomplete in k]


@click.group()
def cli():
    """Jenkins Plugin Generator - creates fast templates of jenkins plugins"""
    pass


@cli.command()
@click.argument('tool_name', type=click.STRING, autocompletion=get_env_vars)
def installer(tool_name):
    """Creates tool-installation & installer"""
    tool_name = util.validate_name_and_create_dir(tool_name)
    if tool_name is not None:
        lib.tool_installation(tool_name)
    else:
        exit(1)


@cli.command(name='util')
@click.argument('tool_name', type=click.STRING, autocompletion=get_env_vars)
def utility(tool_name):
    """Creates utility class with helpful methods"""
    tool_name = util.validate_name_and_create_dir(tool_name)
    if tool_name is not None:
        lib.tool_util(tool_name)
    else:
        exit(1)


@cli.command()
@click.argument('tool_name', type=click.STRING, autocompletion=get_env_vars)
def builder(tool_name):
    """Creates build step"""
    tool_name = util.validate_name_and_create_dir(tool_name)
    if tool_name is not None:
        lib.tool_builder(tool_name)
    else:
        exit(1)


@cli.command()
@click.argument('tool_name', type=click.STRING, autocompletion=get_env_vars)
@click.option('--with-installation', '-I', default=False, is_flag=True,
              help='Generated with a method to help install the tool if necessary')
def wrapper(tool_name, with_installation):
    """Creates wrapper - build environment to install the tool if necessary"""
    tool_name = util.validate_name_and_create_dir(tool_name)
    if tool_name is not None:
        lib.tool_wrapper(tool_name, with_installation)
        if with_installation:
            lib.tool_installation(tool_name)
    else:
        exit(1)


@cli.command()
@click.argument('tool_name', type=click.STRING, autocompletion=get_env_vars)
def publisher(tool_name):
    """Creates post-build action"""
    tool_name = util.validate_name_and_create_dir(tool_name)
    if tool_name is not None:
        lib.tool_publisher(tool_name)
    else:
        exit(1)


@cli.command(name='all')
@click.argument('tool_name', type=click.STRING, autocompletion=get_env_vars)
def make_all(tool_name):
    """Creates it all"""
    tool_name = util.validate_name_and_create_dir(tool_name)
    if tool_name is not None:
        lib.make_all(tool_name)
    else:
        exit(1)
