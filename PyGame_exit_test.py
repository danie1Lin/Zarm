# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:06:17 2017

@author: daniel
"""

import pygame, threading, random

def go():
  pygame.init()
  surf = pygame.display.set_mode((640,480))
  pygame.fastevent.init()

  while True:
    e = pygame.fastevent.poll()
    if e.type == pygame.KEYDOWN and e.unicode == 'q':
      return

    surf.set_at((random.randint(0,640), random.randint(0,480)), (255,255,255))
    pygame.display.flip()

t = threading.Thread(target=go)
t.start()
t.join()