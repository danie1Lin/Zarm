import sys
sys.path.insert(0, "..")

import math
import time
import pygame
import pgu
from pgu import gui, timer
import threading
from websocket import create_connection,setdefaulttimeout

ws = 1



width = 800
height = 800
screen = pygame.display.set_mode((width+400,height))

app = gui.Desktop()
gameArea = gui.Widget(width=width, height=height)
detailArea = gui.Container(width=400)
tbl = gui.Table(height=screen.get_height())
tbl.tr()
tbl.td(gameArea)
tbl.td(detailArea)

table2 = gui.Table()


btn1 = gui.Button("Connect",height=50)
def connect_wifi():
    global ws
    if ws==1:
        try:
            ws = create_connection("ws://192.168.4.1:8266/")
            btn1.value = 'Disconnect'
        except:
            print(u'檢查Wifi是否連接')
            btn1.value = "Connect"
    else:
        ws.close()
        ws = 1
        btn1.value = "Connect"
def estable_connection():
    threading.Thread(target = connect_wifi, args = (), name ='estable_connection').start()
btn1.connect(gui.CLICK,estable_connection)



line = gui.Input(size=49)
def lkey(_event):
    e = _event
    global ws
    if e.key == pygame.K_RETURN:
        val = line.value
        line.value = ''
        line.focus()
        #print('>>> '+val)
        try:
            ws.send(val+'\n\r')
        except:
            print("not connected")
            lines.tr()
            lines.td(gui.Label("Not connect"),align=-1)


        
line.connect(gui.KEYDOWN,lkey)
table2.tr()
lines = gui.Table()
box = gui.ScrollArea(lines,400,500)
table2.td(box, align=-1)
table2.tr()
table2.td(line, align=-1)
table2.tr()
table2.td(btn1, align=-1)


detailArea.add(table2,0,0)

app.init(tbl,screen)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



done = False
clock = pygame.time.Clock()
background_img = pygame.image.load("坐標軸.png").convert()
background_img = pygame.transform.scale(background_img, (width,height))
result = ''
def resv():
    global ws
    global result
    while 1 :
        time.sleep(1)
        print('running')
        while ws != 1:
            try:
                char=''
                result = ''
                result = ws.recv()
                char=char+result
                if len(result) != 1:
                    lines.tr()
                    lines.td(gui.Label(result.strip()),align=-1)
                    continue
                if result !='':
                    while result != '\r':
                        result = ''
                        result = ws.recv()
                        char=char+result
                        if result == '\r':
                            print("1")
                        elif result == '\n':
                            print('2')
                        else:
                            print(result)
                    if char != '\r':
                        print(char)
                        lines.tr()
                        lines.td(gui.Label(char.strip()),align=-1)
                else:
                    print('HaHa')
            except AttributeError:
                print('檢查硬體')
                time.sleep(1)
            except ConnectionResetError:
                print('重新檢查硬體')
                ws.close()
                ws = 1
                time.sleep(1)
            except ConnectionAbortedError:
                print('連線中斷')
                ws.close()
                ws = 1
                time.sleep(1)
            except:
                print ("Unexpected error:", sys.exc_info()[0])
        

        
t_resv = threading.Thread(target = resv, args = (), name ='res')
t_resv.daemon=True
t_resv.start()

z_control = 80

background_position = [0, 0]
XY = []
player_position=[0,0]
x = 0
y = 0 
app.update()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    
    
    pygame.display.flip()
    screen.set_clip()
    lst = app.update()
    updates = []
    if (lst):
        updates += lst
    screen.set_clip((0,0,800,800))
    screen.blit(background_img, background_position)
    ######################################
    '''逆時針畫出arc'''
    pygame.draw.circle(screen,RED,(400,400),10)
    pygame.draw.circle(screen,RED,(400,400),200,5)
    pygame.draw.arc(screen,RED,(0,0,800,800),0,-3.14,5)
    pygame.draw.line(screen,RED,(0,400),(800,400),3)
    ##############################
    for event in pygame.event.get(): # User did something
        app.event(event)
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            pygame.quit()
            if ws != 1:
                ws.close()
            
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            [x_control,y_control] = pygame.mouse.get_pos()
            button = event.button
            if button == 1:
                XY.append((x_control,y_control))
                x_control = x_control - width/2
                y_control = height/2- y_control
                print(x_control,y_control)
            elif button==4:
                z_control=z_control+5
                print( z_control)
            elif button==5:
                z_control=z_control-5
                print (z_control)
        if event.type==pygame.MOUSEMOTION:
            player_position = pygame.mouse.get_pos()
            x = player_position[0]
            y = player_position[1]
            x = x- width/2
            y = height/2- y

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    
    try:
        pygame.draw.circle(screen,GREEN,(player_position[0],player_position[1]),z_control)
    except:
        print("wrong")
    for (x_list,y_list) in XY:
        pygame.draw.circle(screen,RED,(x_list,y_list),10)
        
    myFont = pygame.font.Font('msjh.ttc', 20)
    myText = myFont.render(str(x)+', '+str(y)+','+str(z_control), 1, BLUE)
    
    screen.blit(myText,(player_position[0]+10,player_position[1]-10))
    
    # Copy image to screen: