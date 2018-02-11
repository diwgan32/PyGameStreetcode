"""
 bricka (a breakout clone)
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys
import pygame
SCREEN_SIZE = 640, 480
BLACK = (0, 0, 0)
ORANGE = (255,165,0)

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
        pygame.display.flip()

    def playing_game(self):
        return self.is_playing_game

    def draw_rectangle(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, [x, y, width, height])

    def forward(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing_game = False

        self.clock.tick(50)
        