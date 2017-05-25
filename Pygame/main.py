import pygame
import inputbox
import Tkinter as tk
from Tkinter import *
import os
import platform
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

root = tk.Tk()
embed = tk.Frame(root, width = 360, height = 360) #creates embed frame for pygame window
embed.pack()
buttonwin = tk.Frame(root, width = 500, height = 500)
buttonwin.pack()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

root.update()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
width = 360
height = 360 
screen = pygame.display.set_mode((width,height))

done = False
clock = pygame.time.Clock()
background_img = pygame.image.load("XY.png").convert()
player_image = pygame.image.load("player.png").convert()
# Used to manage how fast the screen updates
player_image.set_colorkey(BLACK)
background_img.set_colorkey(BLACK)
z_control = 80

background_position = [0, 0]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            [x_control,y_control] = pygame.mouse.get_pos()
            button = event.button
            if button == 1:
                x_control = x_control - width/2
                y_control = height/2- y_control
                print(x_control,y_control)
            elif button==4:
                z_control=z_control+5
                print z_control
            elif button==5:
                z_control=z_control-5
                print z_control

    screen.blit(background_img, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
    screen.blit(player_image, [x, y])
    pygame.display.flip()
    root.update()
