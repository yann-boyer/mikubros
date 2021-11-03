"""

W.I.P

"""
import pygame
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
