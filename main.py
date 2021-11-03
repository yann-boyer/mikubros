"""

W.I.P

"""
import sys

import pygame
from sys import exit
from pygame.locals import *

if not pygame.get_init():
    pygame.init()


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("mikubros")

# initialisation of some var
running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("closing mikubros")
            sys.exit()
    # updating content
    pygame.display.update()
    clock.tick(60)
