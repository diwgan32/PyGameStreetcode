"""
 bricka (a breakout clone)
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys
import pygame
from pygame_util import *
import uuid
import numpy as np
import collections

SCREEN_SIZE = 640, 480
BLACK = T(0, 0, 0)
ORANGE = T(255, 165, 0)
PINK = T(255, 192, 203)
RED = T(240, 10, 10)
BLUE = T(0, 0, 255)
YELLOW = T(255, 255, 0)
WHITE = T(255, 255, 255)
    
Point = collections.namedtuple('Point', 'x y')

class Sprite:
    def __init__(self, x, y, width, height, color, uuid):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._velocity = [0, 0]
        self._uuid = uuid

    def get_next_frame_bounding_box(self):
        return [self._x + self._width/2.0 + self._velocity[0],
                self._y + self._height/2.0 + self._velocity[1],
                self._width,
                self._height]

    def get_current_frame_bounding_box(self):
        return [self._x + self._width/2.0,
                self._y + self._height/2.0,
                self._width,
                self._height]

    def uuid(self):
        return self._uuid

    def move(self, velocity):
        self._velocity = velocity

    def reset_velocity(self):
        self._velocity = [0, 0]

    def set_velocity(self, velocity):
        self._velocity = [velocity[0], velocity[1]]

    def apply_velocity(self):
        self._x += self._velocity[0]
        self._y += self._velocity[1]
        self.reset_velocity()

    def get_position(self):
        return Point(x = self._x + self._width/2.0 + self._velocity[0], \
                     y = self._y + self._height/2.0 + self._velocity[1])


class Rectangle(Sprite):
    def __init__(self, x, y, width, height, color, uuid):
        Sprite.__init__(self, x, y, width, height, color, uuid)

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, 
                         pygame.Rect([self._x, self._y, self._width, self._height]))

    

class Circle(Sprite):
    def __init__(self, x, y, radius, color, uuid):
        Sprite.__init__(self, x - radius, y - radius, radius * 2,
                        radius * 2, color, uuid)
        self._radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self._color,
                           (int(self._x + self._radius), int(self._y + self._radius)), self._radius)

    def get_position(self):
        return Point(x = self._x + self._velocity[0], y = self._y + self._velocity[1])

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
        self.screen_color = color
        self.is_playing_game = True
        self.sprites = {}
        
        self.draw_rectangle(0,100,10,1,WHITE)
        self.draw_rectangle(0,200,10,1,WHITE)
        self.draw_rectangle(0,300,10,1,WHITE)
        self.draw_rectangle(0,400,10,1,WHITE)
        self.draw_rectangle(100,0,1,10,WHITE)
        self.draw_rectangle(200,0,1,10,WHITE)
        self.draw_rectangle(300,0,1,10,WHITE)
        self.draw_rectangle(400,0,1,10,WHITE)
        self.draw_rectangle(500,0,1,10,WHITE)
        self.draw_rectangle(600,0,1,10,WHITE)
        self.collision_flag = 0

    def playing_game(self):
        return self.is_playing_game

    def draw_rectangle(self, x, y, width, height, color):
        identity = uuid.uuid4().hex
        rect = Rectangle(x, y, width, height, color, identity)
        self.sprites[identity] = rect
        return rect

    def draw_circle(self, x, y, radius, color):
        identity = uuid.uuid4().hex
        circle = Circle(x, y, radius, color, identity)
        self.sprites[identity] = circle
        return circle      

    def delete(self, shape):
        if(shape.uuid() in self.sprites):
            del self.sprites[shape.uuid()]

    def apply_velocity(self):
        for shape_key in self.sprites:
            self.sprites[shape_key].apply_velocity()

    def forward(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False
        self.screen.fill(self.screen_color)
        self.clock.tick(50)
        self.apply_velocity()
        for uuid in self.sprites:
            self.sprites[uuid].draw(self.screen)

        pygame.display.flip()

    def collided_with(self, shape1, shape2):
        if (shape1.uuid() not in self.sprites or shape2.uuid() not in self.sprites):
            return 

        collide = rect_overlap(shape1.get_next_frame_bounding_box(), 
                               shape2.get_next_frame_bounding_box())
        return collide

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
        if keys[pygame.K_RETURN]:
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


