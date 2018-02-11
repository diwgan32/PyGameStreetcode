"""
Test the library in Screen.py
"""
from Screen import *

display = Screen(BLACK)

while display.playing_game():

    display.draw_rectangle(100, 100, 100, 100, ORANGE)
    display.draw_rectangle(10, 100, 50, 100, BLUE+RED)
    if(display.space_is_pressed()):
        display.draw_rectangle(100, 100, 100, 100, YELLOW)
    display.forward()
