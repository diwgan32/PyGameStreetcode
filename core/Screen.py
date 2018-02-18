"""
 bricka (a breakout clone)
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import pygame
import uuid

from core.pygame_util import *
from core.colors import *
from core.shape import *

SCREEN_SIZE = 640, 480


class Screen:
    def __init__(self, color):
        """
        Create a screen (window) in which you can draw objects.
        """

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
        """
        Draw a rectangle on your screen.
        """

        identity = uuid.uuid4().hex
        rect = Rectangle(x, y, width, height, color, identity)
        self.sprites[identity] = rect
        return rect

    def draw_circle(self, x, y, radius, color):
        """
        Draw a circle on your screen.
        """
        identity = uuid.uuid4().hex
        circle = Circle(x, y, radius, color, identity)
        self.sprites[identity] = circle
        return circle

    def delete(self, shape):
        """
        Delete a shape from the screen
        """

        if(shape.uuid() in self.sprites):
            del self.sprites[shape.uuid()]

    def _apply_velocity(self):
        for shape_key in self.sprites:
            self.sprites[shape_key].apply_velocity()

    def forward(self):
        """
        Move the game on screen one step forward.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False
        self.screen.fill(self.screen_color)
        self.clock.tick(50)
        self._apply_velocity()
        for uuid in self.sprites:
            self.sprites[uuid].draw(self.screen)

        pygame.display.flip()

    def collided_with(self, shape1, shape2):
        """
        Check if two shapes have hit eachother
        """

        if (shape1.uuid() not in self.sprites or shape2.uuid() not in self.sprites):
            return

        collide = rect_overlap(shape1.get_next_frame_bounding_box(),
                               shape2.get_next_frame_bounding_box())
        return collide

    def left_is_pressed(self):
        """
        Return true if the left arrow key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return True
        return False

    def right_is_pressed(self):
        """
        Return true if the right arrow key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            return True
        return False

    def up_is_pressed(self):
        """
        Return true if the up arrow key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return True
        return False

    def down_is_pressed(self):
        """
        Return true if the down arrow key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            return True
        return False

    def space_is_pressed(self):
        """
        Return true if the spacebar is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        return False

    def enter_is_pressed(self):
        """
        Return true if the enter key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        return False

    def w_is_pressed(self):
        """
        Return true if the 'W' key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return True
        return False

    def a_is_pressed(self):
        """
        Return true if the 'A' key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            return True
        return False

    def s_is_pressed(self):
        """
        Return true if the 'S' key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            return True
        return False

    def d_is_pressed(self):
        """
        Return true if the 'D' key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            return True
        return False

    def shift_is_pressed(self):
        """
        Return true if the shift key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
            return True
        return False

    def tab_is_pressed(self):
        """
        Return true if the tab key is being pressed.
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            return True
        return False


