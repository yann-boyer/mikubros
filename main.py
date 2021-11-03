"""

W.I.P

"""
import sys
from settings import *
import pygame
from Overworld import *
from sys import exit
from pygame.locals import *

class Game:
    def __init__(self):
        self.max_level = 1
        self.overworld = Overworld(0,self.max_level,screen)

    def run(self):
        self.overworld.run()

if not pygame.get_init():
    pygame.init()


screen = pygame.display.set_mode((screen_with, screen_height))
pygame.display.set_caption("mikubros")
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

# initialisation of some var
running = True
clock = pygame.time.Clock()
game = Game()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("closing mikubros")
            sys.exit()
    game.run()
    # updating content
    pygame.display.update()
    clock.tick(60)
