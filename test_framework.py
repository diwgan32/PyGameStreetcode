"""
Test the library in Screen.py
"""
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
new_shape = display.draw_rectangle(10, 100, 50, 100, BLUE)
projectiles = []
while display.playing_game():
    if(display.right_is_pressed()):
        display.move(my_shape,[3,0])
    if(display.left_is_pressed()):
        display.move(my_shape,[-3,0])
    if(display.up_is_pressed()):
        display.move(my_shape,[0, -3])
    if(display.down_is_pressed()):
        display.move(my_shape,[0, 3])
    if(display.enter_is_pressed()):
        display.delete(my_shape)
    if(display.space_is_pressed()):
        x = display.get_position(my_shape).x
        y = display.get_position(my_shape).y
        bullet = display.draw_rectangle(x, y, 20, 20, RED)
        projectiles.append(bullet)
    for bullet in projectiles:
        display.move(bullet,[-10,0])
        if(display.collided_with(bullet, new_shape)):
            display.delete(new_shape)
    if (display.collided_with(my_shape, new_shape)):
        display.move(my_shape, [0, 0])
    display.forward()

