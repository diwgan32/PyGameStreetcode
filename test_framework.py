"""
Test the library in Screen.py
"""
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
new_shape = display.draw_rectangle(10, 100, 50, 100, ORANGE)

while display.playing_game():
    if(display.right_is_pressed()):
       display.move(my_shape,[10,0])
    if(display.left_is_pressed()):
       display.move(my_shape,[-10,0])
    if(display.space_is_pressed()):
        display.delete(my_shape)
    if(display.enter_is_pressed()):
        display.get_position(my_shape)
    display.forward()
