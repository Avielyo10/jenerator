#!/usr/bin/env python3
import os
from . import util

CWD = os.getcwd()+"/"


def replace_and_write(tool_name, src_path, dest_path, old_word, new_word):
    this_dir, this_filename = os.path.split(__file__)
    DATA_FILE = os.path.join(this_dir, "files", src_path)
    with open(DATA_FILE, "rt") as txt:
        with open(dest_path, "wt") as java:
            for line in txt:
                java.write(line.replace(
                    old_word, new_word))


def replace_and_write2(tool_name, src_path, dest_path, old_word1, new_word1, old_word2, new_word2):
    this_dir, this_filename = os.path.split(__file__)
    DATA_FILE = os.path.join(this_dir, "files", src_path)
    with open(DATA_FILE, "rt") as txt:
        with open(dest_path, "wt") as java:
            for line in txt:
                if old_word1 in line:
                    java.write(
                        line.replace(old_word1, new_word1))
                else:
                    java.write(line.replace(
                        old_word2, new_word2))


def tool_installation(tool_name):
    dest = tool_name+"/Installation/"
    util.create_dir(dest)
    dest = CWD + dest + tool_name
    if not os.path.exists(dest + "Installer.java"):
        replace_and_write(tool_name, "$TOOL+INSTALLER.txt",
                          dest + "Installer.java", "$TOOL+INSTALLER", tool_name+"Installer")

    if not os.path.exists(dest + "Tool.java"):
        replace_and_write2(tool_name, "$TOOL+INSTALLATION.txt", dest + "Tool.java",
                           "$TOOL+NAME", tool_name, "$TOOL+INSTALLATION", tool_name+"Tool")


def tool_util(tool_name):
    dest = tool_name+"/util/"
    util.create_dir(dest)
    dest = CWD + dest + tool_name
    if not os.path.exists(dest + "Util.java"):
        replace_and_write(tool_name, "$TOOL+UTIL.txt",
                          dest + "Util.java", "$TOOL+UTIL", tool_name+"Util")


def tool_builder(tool_name):
    dest = CWD + tool_name + "/" + tool_name + "Builder.java"
    if not os.path.exists(dest):
        replace_and_write(tool_name, "$TOOL+BUILDER.txt",
                          dest, "$TOOL+BUILDER", tool_name+"Builder")


def tool_wrapper(tool_name, with_installation):
    dest = CWD + tool_name + "/" + tool_name + "Wrapper.java"
    if not os.path.exists(dest):
        if with_installation:
            replace_and_write2(tool_name, "$TOOL+WRAPPER+INSTALLRER.txt", dest, "$TOOL+INSTALLATION",
                               tool_name+"Tool", "$TOOL+WRAPPER", tool_name+"Wrapper")
        else:
            replace_and_write(tool_name, "$TOOL+WRAPPER.txt",
                              tool_name+"Tool", "$TOOL+WRAPPER", tool_name+"Wrapper")


def tool_publisher(tool_name):
    dest = CWD + tool_name + "/" + tool_name + "Publisher.java"
    if not os.path.exists(dest):
        replace_and_write(tool_name, "$TOOL+PUBLISHER.txt",
                          dest, "$TOOL+PUBLISHER", tool_name+"Publisher")


def make_all(tool_name):
    tool_installation(tool_name)
    tool_wrapper(tool_name, True)
    tool_builder(tool_name)
    tool_publisher(tool_name)
    tool_util(tool_name)
