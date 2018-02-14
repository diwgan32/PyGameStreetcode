"""
Test the library in Screen.py
"""
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
#new_shape = display.draw_rectangle(10, 100, 50, 100, ORANGE)
projectiles = []
while display.playing_game():
    if(display.right_is_pressed()):
       display.move(my_shape,[10,0])
    if(display.left_is_pressed()):
       display.move(my_shape,[-10,0])
    if(display.enter_is_pressed()):
        display.delete(my_shape)
    if(display.space_is_pressed()):
        pos = display.get_position(my_shape)
        bullet = display.draw_rectangle(pos[0], pos[1], 20, 20, RED)
        projectiles.append(bullet)
    for bullet in projectiles:
        display.move(bullet,[20,0])
    display.forward()
