# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:41:58 2017

@author: daniel
"""

"""
參考資料
http://osdcpapers.cgpublisher.com/product/pub.84/prod.11/m.1?
"""
import pygame
from pygame.locals import *
import threading
from multiprocessing import Process
pygame.init()
screen = pygame.display.set_mode((1024,768))

car = pygame.image.load('mini-suv-512.png')
screen.blit(car,(50,100))
pygame.display.flip()

def handle_event():
        while True:
            pygame.mainloop(0.1)
threading.Thread(target = handle_event , args = (), name ='res').start()

