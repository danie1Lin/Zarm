# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 21:42:49 2017

@author: daniel
"""
import threading
import time
from websocket import create_connection,setdefaulttimeout
a = 2 
def change() :
    print('yo')
    global a
    print('yo',id(a),a)
    try:
        a = create_connection("ws://192.168.4.1:8266/")
    except:
        print('fail')
    call()

def call():
    global a
    print('ss',id(a),a)