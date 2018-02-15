"""
    Test the library in Screen.py
    """
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
my_pusheen = display.draw_rectangle(400, 300, 50, 80, RED)
unicorns=[]
while display.playing_game():
    if(display.right_is_pressed()):
        display.move(my_shape,[3,0])
    if(display.left_is_pressed()):
        display.move(my_shape,[-3,0])
    if(display.up_is_pressed()):
        display.move(my_shape,[0, -3])
    if(display.down_is_pressed()):
        display.move(my_shape,[0, 3])
    if(display.space_is_pressed()):
        x=display.get_position(my_shape).x
        y=display.get_position(my_shape).y
        unicorn = display.draw_rectangle(x,y,10,5, PINK)
        unicorns.append(unicorn)
    if(display.collided_with(my_pusheen, my_shape)):
        display.move(my_shape,[0,0])
    for unicorn in unicorns:
        display.move(unicorn,[3,0])
        if(display.collided_with(my_pusheen,unicorn)):
            display.delete(my_pusheen)
    display.forward()
