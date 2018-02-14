"""
Test the library in Screen.py
"""
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
new_shape = display.draw_rectangle(10, 100, 50, 100, BLUE)

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
		display.delete(my_shape)
	if(display.enter_is_pressed()):
		display.get_position(my_shape)
	if (display.collided_with(my_shape, new_shape)):
		display.move(my_shape, [0, 0])
	
	display.forward()
