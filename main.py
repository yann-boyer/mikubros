"""

W.I.P

"""
import sys

import pygame
from sys import exit
from pygame.locals import *

if not pygame.get_init():
    pygame.init()

pygame.display.set_caption("mikubros")
pygame.display.set_mode((1280, 720))


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("closing mikubros")
            sys.exit()
    # updating content
    pygame.display.update()
