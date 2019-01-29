# main.py - useful module of main
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import time

from six.moves import input

zzz_banner = """
 _ ____        _             
(_)___ \ _ __ | |____________
| | __) | '_ \| |_  /_  /_  /
| |/ __/| |_) | |/ / / / / / 
|_|_____| .__/| /___/___/___|
        |_|   |_|            

"""
backtomenu_banner = """
  [99] Главное меню
  [00] Выход
"""


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()


def backtomenu_option():
    print(backtomenu_banner)
    backtomenu = input("$zzz ")

    if backtomenu == "99":
        restart_program()
    elif backtomenu == "00":
        sys.exit()
    else:
        print("\nERROR: Неправильный Ввод")
        time.sleep(2)
        restart_program()


def banner():
    print(zzz_banner)
