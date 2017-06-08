
#!/usr/bin/env python
# -*- coding: big5 -*-
import pygame
import Buttons
from pygame.locals import *
from websocket import create_connection
# the following line is not needed if pgu is installed
import sys; sys.path.insert(0, "..")

import traceback
import time
import threading
from pgu import gui
from pgu import html
ws = 1
screen = pygame.display.set_mode((200,100),SWSURFACE)

def connect():
    global ws
    try:
        ws = create_connection("ws://192.168.4.1:8266/")
        wifi_connect.value='以連結'.encode('utf-8')
    except:
        print(u'檢查Wifi是否連接')

class StringStream:
    def __init__(self):
        self._data = ''
    def write(self,data):
        self._data = self._data+data
        _lines = self._data.split("\n")
        for line in _lines[:-1]:
            lines.tr()
            lines.td(gui.Label(str(line)),align=-1)
        self._data = _lines[-1:][0]
        
_locals = {}
def lkey(_event):
    e = _event
    global ws
    if e.key == K_RETURN:
        
        
        val = line.value
        line.value = ''
        line.focus()
        #print('>>> '+val)
        try:
            ws.send(val+'\n\r')
        except:
            print("not connected")
            #code = compile(val,'<string>','single')
            #eval(code,globals(),_locals)0        ws.send(val+'\r\n')
        




def resv():
    global ws
    while 1 :
        try:
            result =  ws.recv()
            char=''
            if result != '' :
                while result != '\n':
                    char=char+result
                    result =  ws.recv()
                char=char+result
                _stdout = sys.stdout
                s = sys.stdout = StringStream()
                print(char)
                sys.stdout = _stdout
        except:
            print('No')
            time.sleep(1)
    
app = gui.Desktop()
t = gui.Table(width=800,height=800)
t.tr()
wifi_connect = gui.Button("連接")
wifi_connect.connect(gui.CLICK,connect)
t.td(wifi_connect)

t.tr()
lines = gui.Table()
box = gui.ScrollArea(lines,500,380)
t.td(box)

t.tr()
line = gui.Input(size=49)
line.connect(gui.KEYDOWN,lkey)
t.td(line)
t.tr()

pygame.init()
Button1 = Buttons.Button()
Button1.create_button(screen,(107,142,35),0,0,20,10,0,"連接", (255,255,255))
pygame.display.flip()

class Hack(gui.Spacer):
    def resize(self,width=None,height=None):
        box.set_vertical_scroll(65535)
        return 1,1
    

t.td(Hack(1,1))

app.connect(gui.QUIT,app.quit,None)
app.init(t)
threading.Thread(target = resv, args = (), name ='res').start()
app.run()