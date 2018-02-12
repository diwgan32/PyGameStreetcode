"""
 bricka (a breakout clone)
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys
import pygame
from pygame_util import *
import uuid

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
        self.screen_color = color
        self.is_playing_game = True
        self.sprites = {}

    def playing_game(self):
        return self.is_playing_game

    def create_shape_dictionary(self, properties, shape_type, color, uuid):
        return {'attr': properties, 'type': shape_type, 'color': color, 'uuid': uuid}

    def draw_rectangle(self, x, y, width, height, color):
        identity = uuid.uuid4().hex
        new_rect = self.create_shape_dictionary([x, y, width, height], "rect", color, identity)
        self.sprites[identity] = new_rect
        return new_rect

    def draw_image(self, file_name, x, y):
        identity = uuid.uuid4().hex
        myimage = pygame.image.load(file_name)
        myimage.convert()
        new_sprite = self.create_shape_dictionary([x, y, myimage], "sprite", (0, 0, 0), identity)

    def move(self, shape_to_move, other):
        if (shape_to_move['type'] == "rect"):
            del self.sprites[shape_to_move['uuid']]
            new_rect = self.create_shape_dictionary([shape_to_move['attr'][0] + other[0],\
                                                shape_to_move['attr'][1] + other[1],\
                                                shape_to_move['attr'][2], shape_to_move['attr'][3]], 
                                               shape_to_move['type'], shape_to_move['color'],
                                               shape_to_move['uuid'])

            shape_to_move['attr'] = [shape_to_move['attr'][0] + other[0],\
                                     shape_to_move['attr'][1] + other[1],\
                                     shape_to_move['attr'][2], shape_to_move['attr'][3]]
            self.sprites[shape_to_move['uuid']] = new_rect
        if (shape_to_move['type'] == "sprite"):
            del self.sprites[shape_to_move['uuid']]
            new_rect = self.create_shape_dictionary([shape_to_move['attr'][0] + other[0],\
                                                shape_to_move['attr'][1] + other[1],\
                                                shape_to_move['attr'][2]], 
                                               shape_to_move['type'], shape_to_move['color'],
                                               shape_to_move['uuid'])

            shape_to_move['attr'] = [shape_to_move['attr'][0] + other[0],\
                                     shape_to_move['attr'][1] + other[1],\
                                     shape_to_move['attr'][2]]
            self.sprites[shape_to_move['uuid']] = new_rect

    def forward(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False
        self.screen.fill(self.screen_color)
        self.clock.tick(50)
        for uuid in self.sprites:
            if (self.sprites[uuid]['type'] == "rect"):
                pygame.draw.rect(self.screen, self.sprites[uuid]['color'], 
                                 pygame.Rect(self.sprites[uuid]['attr']))
            if (self.sprites[uuid]['type'] == "sprite"):
                self.screen.blit(self.sprites['uuid']['attr'][2], (self.sprites['uuid']['attr'][0],\
                                                                   self.sprites['uuid']['attr'][1]))

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

