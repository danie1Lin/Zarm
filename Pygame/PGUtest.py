"""an example a python console"""

import pygame

from pygame.locals import *
from websocket import create_connection
# the following line is not needed if pgu is installed
import sys; sys.path.insert(0, "..")

import traceback
import time
import threading
from pgu import gui
from pgu import html

ws = create_connection("ws://192.168.4.1:8266/")

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
    if e.key == K_RETURN:
        
        
        val = line.value
        line.value = ''
        line.focus()
        #print('>>> '+val)
        ws.send(val+'\n\r')
            #code = compile(val,'<string>','single')
            #eval(code,globals(),_locals)0        ws.send(val+'\r\n')
        




def resv():
    while 1 :
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
    
app = gui.Desktop()
t = gui.Table(width=800,height=800)

t.tr()
lines = gui.Table()
box = gui.ScrollArea(lines,500,380)
t.td(box)

t.tr()
line = gui.Input(size=49)
line.connect(gui.KEYDOWN,lkey)
t.td(line)
t.tr()
class Hack(gui.Spacer):
    def resize(self,width=None,height=None):
        box.set_vertical_scroll(65535)
        return 1,1
t.td(Hack(1,1))

app.connect(gui.QUIT,app.quit,None)
app.init(t)
threading.Thread(target = resv, args = (), name ='res').start()
app.run()
    
