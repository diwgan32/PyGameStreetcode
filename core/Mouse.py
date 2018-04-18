import pygame
import math
from Sprite import *

class Mouse:
    def __init__(self):
        self.pressed = {}
        self.released = {}

    def get_position(self):
        return pygame.mouse.get_pos()

    def ontop(self, sprite):
        mx, my =  pygame.mouse.get_pos()
        sx, sy = sprite.get_position()
        if isinstance(sprite, Circle):
            return math.sqrt((mx-sx)**2 + (my-sy)**2) < sprite._radius
        else:
            sw = sprite._width/2.0
            sh = sprite._height/2.0
            return mx > sx-sw and my > sy-sh and mx < sx+sw and my < sy+sh

    def left_is_down(self):
        buttons = pygame.mouse.get_pressed()
        return buttons[0]==1

    def right_is_down(self):
        buttons = pygame.mouse.get_pressed()
        return buttons[2]==1

    def left_is_pressed(self):
        return 1 in self.pressed

    def right_is_pressed(self):
        return 3 in self.pressed

    def left_is_released(self):
        return 1 in self.released

    def right_is_released(self):
        return 3 in self.released
