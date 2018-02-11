"""
Test the library in Screen.py
"""
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
new_shape = display.draw_rectangle(10, 100, 50, 100, ORANGE)

while display.playing_game():
    display.move(my_shape, [0, -1])
    display.forward()
