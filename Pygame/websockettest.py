import websocket
import thread
import time
import sys
from pgu import gui

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print (error)

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    def run(*args):
        time.sleep(1)
    thread.start_new_thread(run, ())



if __name__ == '__main__':
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp("ws://192.168.4.1:8266/",
	                          on_message = on_message,
	                          on_error = on_error,
	                          on_close = on_close)
	ws.on_open = on_open

