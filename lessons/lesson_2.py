"""
    Test the library in Screen.py
    """
import sys
sys.path.insert(0, '../core')
from Screen import *

display = Screen(BLACK)
keyboard = display.get_keyboard()
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)

while display.playing_game():
    if(keyboard.right_is_down()):
        my_shape.move([3,0])
    if(keyboard.left_is_down()):
        my_shape.move([-3,0])
    if(keyboard.up_is_down()):
        my_shape.move([0,-3])
    if(keyboard.down_is_down()):
        my_shape.move([0,3])
    display.forward()

