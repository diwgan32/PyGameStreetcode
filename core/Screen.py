import sys
import pygame
import uuid
import numpy as np
import collections
import copy

from Sprite import *
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
        self.pressed = [0,]*1000
        self.released = [0,]*1000
        #print(self.prior_key_states[pygame.K_SPACE])



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

    def delete(self, shape):
        if(shape.uuid() in self.sprites):
            del self.sprites[shape.uuid()]

    def apply_velocity(self):
        for shape_key in self.sprites:
            self.sprites[shape_key].apply_velocity()

    def forward(self):
        self.pressed=[0,]*1000
        self.released=[0,]*1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                #print(event.key)
                self.pressed[event.key]=1
            if event.type == pygame.KEYUP:
                #if event.key == pygame.K_SPACE:
                #print(event.key)
                self.released[event.key]=1
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

    def left_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return True
        return False

    def right_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            return True
        return False

    def up_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return True
        return False

    def down_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            return True
        return False

    def space_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        return False

    def enter_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        return False

    def w_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return True
        return False

    def a_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            return True
        return False

    def s_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            return True
        return False

    def d_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            return True
        return False

    def shift_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
            return True
        return False

    def tab_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            return True
        return False

    def q_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            return True
        return False

    def e_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            return True
        return False

    def r_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return True
        return False

    def t_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            return True
        return False

    def y_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            return True
        return False

    def u_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u]:
            return True
        return False

    def i_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i]:
            return True
        return False

    def o_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:
            return True
        return False

    def p_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            return True
        return False

    def f_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            return True
        return False

    def g_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            return True
        return False

    def h_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_h]:
            return True
        return False

    def j_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            return True
        return False

    def k_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            return True
        return False

    def l_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            return True
        return False

    def z_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            return True
        return False

    def x_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            return True
        return False

    def c_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            return True
        return False

    def v_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_v]:
            return True
        return False

    def b_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            return True
        return False

    def n_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            return True
        return False

    def m_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            return True
        return False

    def j_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            return True
        return False




    def space_is_pressed(self):
        if self.pressed[pygame.K_SPACE]:
            return True
        return False

    def space_is_released(self):
        if self.released[pygame.K_SPACE]:
            return True
        return False

    def a_is_pressed(self):
        if self.pressed[pygame.K_a]:
            return True
        return False

    def a_is_released(self):
        if self.released[pygame.K_a]:
            return True
        return False

    def b_is_pressed(self):
        if self.pressed[pygame.K_b]:
            return True
        return False

    def b_is_released(self):
        if self.released[pygame.K_b]:
            return True
        return False
    def c_is_pressed(self):
        if self.pressed[pygame.K_c]:
            return True
        return False

    def c_is_released(self):
        if self.released[pygame.K_c]:
            return True
        return False
    def d_is_pressed(self):
        if self.pressed[pygame.K_d]:
            return True
        return False

    def d_is_released(self):
        if self.released[pygame.K_d]:
            return True
        return False
    def e_is_pressed(self):
        if self.pressed[pygame.K_e]:
            return True
        return False

    def e_is_released(self):
        if self.released[pygame.K_e]:
            return True
        return False
    def f_is_pressed(self):
        if self.pressed[pygame.K_f]:
            return True
        return False

    def f_is_released(self):
        if self.released[pygame.K_f]:
            return True
        return False
    def g_is_pressed(self):
        if self.pressed[pygame.K_g]:
            return True
        return False

    def g_is_released(self):
        if self.released[pygame.K_g]:
            return True
        return False
    def h_is_pressed(self):
        if self.pressed[pygame.K_h]:
            return True
        return False

    def h_is_released(self):
        if self.released[pygame.K_h]:
            return True
        return False
    def i_is_pressed(self):
        if self.pressed[pygame.K_i]:
            return True
        return False

    def i_is_released(self):
        if self.released[pygame.K_i]:
            return True
        return False
    def j_is_pressed(self):
        if self.pressed[pygame.K_j]:
            return True
        return False

    def j_is_released(self):
        if self.released[pygame.K_j]:
            return True
        return False
    def k_is_pressed(self):
        if self.pressed[pygame.K_k]:
            return True
        return False

    def k_is_released(self):
        if self.released[pygame.K_k]:
            return True
        return False
    def l_is_pressed(self):
        if self.pressed[pygame.K_l]:
            return True
        return False

    def l_is_released(self):
        if self.released[pygame.K_l]:
            return True
        return False
    def m_is_pressed(self):
        if self.pressed[pygame.K_m]:
            return True
        return False

    def m_is_released(self):
        if self.released[pygame.K_m]:
            return True
        return False
    def n_is_pressed(self):
        if self.pressed[pygame.K_n]:
            return True
        return False

    def n_is_released(self):
        if self.released[pygame.K_n]:
            return True
        return False
    def o_is_pressed(self):
        if self.pressed[pygame.K_o]:
            return True
        return False

    def o_is_released(self):
        if self.released[pygame.K_o]:
            return True
        return False
    def p_is_pressed(self):
        if self.pressed[pygame.K_p]:
            return True
        return False

    def p_is_released(self):
        if self.released[pygame.K_p]:
            return True
        return False
    def q_is_pressed(self):
        if self.pressed[pygame.K_q]:
            return True
        return False

    def q_is_released(self):
        if self.released[pygame.K_q]:
            return True
        return False
    def r_is_pressed(self):
        if self.pressed[pygame.K_r]:
            return True
        return False

    def r_is_released(self):
        if self.released[pygame.K_r]:
            return True
        return False
    def s_is_pressed(self):
        if self.pressed[pygame.K_s]:
            return True
        return False

    def s_is_released(self):
        if self.released[pygame.K_s]:
            return True
        return False
    def t_is_pressed(self):
        if self.pressed[pygame.K_t]:
            return True
        return False

    def t_is_released(self):
        if self.released[pygame.K_t]:
            return True
        return False

    def u_is_pressed(self):
        if self.pressed[pygame.K_u]:
            return True
        return False

    def u_is_released(self):
        if self.released[pygame.K_u]:
            return True
        return False
    def v_is_pressed(self):
        if self.pressed[pygame.K_v]:
            return True
        return False

    def v_is_released(self):
        if self.released[pygame.K_v]:
            return True
        return False

    def w_is_pressed(self):
        if self.pressed[pygame.K_w]:
            return True
        return False

    def w_is_released(self):
        if self.released[pygame.K_w]:
            return True
        return False

    def x_is_pressed(self):
        if self.pressed[pygame.K_x]:
            return True
        return False

    def x_is_released(self):
        if self.released[pygame.K_x]:
            return True
        return False

    def y_is_pressed(self):
        if self.pressed[pygame.K_y]:
            return True
        return False

    def y_is_released(self):
        if self.released[pygame.K_y]:
            return True
        return False

    def z_is_pressed(self):
        if self.pressed[pygame.K_z]:
            return True
        return False

    def z_is_released(self):
        if self.released[pygame.K_z]:
            return True
        return False

    def left_is_pressed(self):
        if self.pressed[pygame.K_LEFT]:
            return True
        return False

    def left_is_released(self):
        if self.released[pygame.K_LEFT]:
            return True
        return False

    def right_is_pressed(self):
        if self.pressed[pygame.K_RIGHT]:
            return True
        return False

    def right_is_released(self):
        if self.released[pygame.K_RIGHT]:
            return True
        return False

    def down_is_pressed(self):
        if self.pressed[pygame.K_DOWN]:
            return True
        return False

    def down_is_released(self):
        if self.released[pygame.K_DOWN]:
            return True
        return False

    def up_is_pressed(self):
        if self.pressed[pygame.K_UP]:
            return True
        return False

    def up_is_released(self):
        if self.released[pygame.K_UP]:
            return True
        return False

    def tab_is_pressed(self):
        if self.pressed[pygame.K_TAB]:
            return True
        return False

    def tab_is_released(self):
        if self.released[pygame.K_TAB]:
            return True
        return False
