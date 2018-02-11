"""
Test the library in Screen.py
"""
from Screen import *

display = Screen(BLACK)
while display.playing_game():    
    display.draw_rectangle(100, 100, 100, 100, ORANGE)

    pygame.display.flip()
    display.forward()