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
    
Point = collections.namedtuple('Point', 'x y')

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
        self.collision_flag = 0

    def playing_game(self):
        return self.is_playing_game

    def create_shape_dictionary(self, properties, shape_type, color, uuid):
        return {'attr': properties, 'type': shape_type, 'color': color, 'uuid': uuid}

    def draw_rectangle(self, x, y, width, height, color):
        identity = uuid.uuid4().hex
        new_rect = self.create_shape_dictionary([x, y, width, height], "rect", color, identity)
        self.sprites[identity] = new_rect
        return identity

    def draw_image(self, file_name, x, y):
        identity = uuid.uuid4().hex
        myimage = pygame.image.load(file_name)
        myimage.convert()
        new_sprite = self.create_shape_dictionary([x, y, myimage], "sprite", (0, 0, 0), identity)

    def move(self, shape_key, other):
        try:
            shape_to_move = self.sprites[shape_key]
        except:
            return
        if (self.sprites[shape_key]['type'] == "rect"):
            self.sprites[shape_key]['velocity'] = other

    def delete(self, shape):
        if(shape in self.sprites):
            del self.sprites[shape]

    def get_position(self, shape):
        if(shape in self.sprites):
            return Point(x = self.sprites[shape]['attr'][0] + self.sprites[shape]['attr'][2]/2.0, \
                         y = self.sprites[shape]['attr'][1] + self.sprites[shape]['attr'][3]/2.0)

    def apply_velocity(self):
        for shape_key in self.sprites:
            velocity = [0, 0]
            try:
                velocity = self.sprites[shape_key]['velocity']
                self.sprites[shape_key]['velocity'] = [0, 0]
            except:
                pass
            self.sprites[shape_key]['attr'] = [self.sprites[shape_key]['attr'][0] + velocity[0],\
                                               self.sprites[shape_key]['attr'][1] + velocity[1],\
                                               self.sprites[shape_key]['attr'][2],
                                               self.sprites[shape_key]['attr'][3]]


    def forward(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False
        self.screen.fill(self.screen_color)
        self.clock.tick(50)
        self.apply_velocity()
        for uuid in self.sprites:
            if (self.sprites[uuid]['type'] == "rect"):
                pygame.draw.rect(self.screen, self.sprites[uuid]['color'], 
                                 pygame.Rect(self.sprites[uuid]['attr']))
            if (self.sprites[uuid]['type'] == "sprite"):
                self.screen.blit(self.sprites['uuid']['attr'][2], (self.sprites['uuid']['attr'][0],\
                                                                   self.sprites['uuid']['attr'][1]))
        pygame.display.flip()

    def _test_overlap(self, A, B):
        w = 0.5 * (A[2] + B[2]);
        h = 0.5 * (A[3] + B[3]);
        dx = A[0] - B[0];
        dy = A[1] - B[1];

        if (abs(dx) <= w and abs(dy) <= h):
        
            wy = w * dy;
            hx = h * dx;

            if (wy > hx):
                if (wy > -hx):
                    return True
                else:
                    return True
            else:
                if (wy > -hx):
                    return True
                else:
                    return True
        return False

    def collided_with(self, shape1_key, shape2_key):
        if (shape1_key not in self.sprites or shape2_key not in self.sprites):
            return 
        shape1 = self.sprites[shape1_key]
        shape2 = self.sprites[shape2_key]
        velocity1 = [0, 0]
        velocity2 = [0, 0]
        try:
            velocity1 = shape1['velocity']
            velocity2 = shape2['velocity']
        except:
            pass

        rect1 = [shape1['attr'][0] + shape1['attr'][2]/2.0 + velocity1[0],
                 shape1['attr'][1] + shape1['attr'][3]/2.0 + velocity1[1],
                 shape1['attr'][2],
                 shape1['attr'][3]]

        rect2 = [shape2['attr'][0] + shape2['attr'][2]/2.0 + velocity2[0],
                 shape2['attr'][1] + shape2['attr'][3]/2.0 + velocity2[1],
                 shape2['attr'][2],
                 shape2['attr'][3]]
        collide = self._test_overlap(rect1, rect2)
        
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

