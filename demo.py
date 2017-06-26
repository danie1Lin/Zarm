# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:21:14 2017

@author: daniel
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()