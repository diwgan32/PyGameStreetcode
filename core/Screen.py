import sys
import pygame
import uuid
import numpy as np
import collections
import copy

from Sprite import *
from Keyboard import *
from constants import *
from pygame_util import *

class Screen:
    def __init__(self, color, title="StreetCode Academy"):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(title)

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
        self._keyboard = Keyboard()



    def playing_game(self):
        return self.is_playing_game

    def quit(self):
        self.is_playing_game = False

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

    def draw_text(self, x, y, text, color, font='arial', size=30):
        identity = uuid.uuid4().hex
        text_object = Text(x, y, text, color, identity, font, size)
        self.sprites[identity] = text_object
        return text_object

    def draw_image(self, x, y, image):
        identity = uuid.uuid4().hex
        image_object = Image(x, y, image, identity)
        self.sprites[identity] = image_object
        return image_object

    def delete(self, shape):
        if(shape.uuid() in self.sprites):
            del self.sprites[shape.uuid()]

    def apply_velocity(self):
        for shape_key in self.sprites:
            self.sprites[shape_key].apply_velocity()

    def forward(self):
        self._keyboard.pressed=[0,]*1000
        self._keyboard.released=[0,]*1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                #print(event.key)
                self._keyboard.pressed[event.key]=1
            if event.type == pygame.KEYUP:
                #if event.key == pygame.K_SPACE:
                #print(event.key)
                self._keyboard.released[event.key]=1
        self.screen.fill(self.screen_color)
        self.clock.tick(50)
        self.apply_velocity()
        for uuid in self.sprites:
            self.sprites[uuid].draw(self.screen)
        #self.prior_key_states = tuple(pygame.key.get_pressed())
        pygame.display.flip()

    def collided_with(self, shape1, shape2):
        if (shape1.uuid() not in self.sprites or shape2.uuid() not in self.sprites):
            return

        collide = rect_overlap(shape1.get_next_frame_bounding_box(),
                               shape2.get_next_frame_bounding_box())
        return collide

    def get_keyboard(self):
        return self._keyboard
