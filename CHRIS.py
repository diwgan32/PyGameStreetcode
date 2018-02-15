"""
    Test the library in Screen.py
    """
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
to_do_list= []

while display.playing_game():
    if(display.right_is_pressed()):
        display.move(my_shape,[3,0])
    if(display.left_is_pressed()):
        display.move(my_shape,[-3,0])
    if(display.up_is_pressed()):
        display.move(my_shape,[0, -3])
    if(display.down_is_pressed()):
        display.move(my_shape,[0, 3])
    print(display.get_position(my_shape).x)
    if(display.space_is_pressed()):
        calorie = display.draw_rectangle(display.get_position(my_shape).x,display.get_position(my_shape).y,95,95,BLUE)
        to_do_list.append(calorie)
    for calorie in to_do_list:
        display.move(calorie,[0,-5]) 
        

                     
    display.forward()

