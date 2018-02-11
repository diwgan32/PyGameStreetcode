"""
 bricka (a breakout clone)
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys
import pygame
SCREEN_SIZE = 640, 480
BLACK = (0, 0, 0)
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

    def forward(self):
        self.clock.tick(50)
        self.screen.fill(self.color)