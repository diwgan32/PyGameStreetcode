"""
 bricka (a breakout clone)
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys
import pygame
from pygame_util import *

SCREEN_SIZE = 640, 480
BLACK = T(0, 0, 0)
ORANGE = T(255, 165, 0)
PINK = T(255, 192, 203)
RED = T(240, 10, 10)
BLUE = T(0, 0, 255)
YELLOW = T(255, 255, 0)


class Screen:
    def __init__(self, color):
        pygame.init()   
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("StreetCode Academy")

        self.clock = pygame.time.Clock()

        if pygame.font:
            self.font = pygame.font.Font(None,30)
        else:
            self.font = None
        self.color = color
        self.screen.fill(self.color)
        self.is_playing_game = True
        

    def playing_game(self):
        return self.is_playing_game

    def draw_rectangle(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, [x, y, width, height])

    def forward(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False

        self.clock.tick(50)
        pygame.display.flip()
                
    def left_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return True
        return False

    def right_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            return True
        return False

    def up_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return True
        return False

    def down_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            return True
        return False

    def space_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        return False

    def enter_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ENTER]:
            return True
        return False

    def w_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return True
        return False

    def a_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            return True
        return False

    def s_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            return True
        return False

    def d_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            return True
        return False

    def shift_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
            return True
        return False

    def tab_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            return True
        return False

