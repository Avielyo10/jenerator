#!/usr/bin/env python3
import os


def create_dir(dir_name):
    try:
        os.mkdir(os.getcwd()+"/"+dir_name)
    except:
        pass


def dir_exist(dir_name):
    flag = False
    if os.path.isdir(dir_name) and os.path.exists(dir_name):
        flag = True
    return flag


def change_name_if_needed(name):
    valid = False
    try:
        int(name)
    except:
        valid = True
    if valid:
        return name.title()
    else:
        return None


def validate_name_and_create_dir(tool_name):
    name = change_name_if_needed(tool_name)
    if (name is not None) and (not dir_exist(tool_name)):
        create_dir(name)
    return name
