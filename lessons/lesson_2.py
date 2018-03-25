"""
    Test the library in Screen.py
    """
import sys
sys.path.insert(0, '../core')
from Screen import *

display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)

while display.playing_game():
    if(display.right_is_down()):
        my_shape.move([3,0])
    if(display.left_is_down()):
        my_shape.move([-3,0])
    if(display.up_is_down()):
        my_shape.move([0,-3])
    if(display.down_is_down()):
        my_shape.move([0,3])
    display.forward()

