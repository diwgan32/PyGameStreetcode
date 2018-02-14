"""
Test the library in Screen.py
"""
from Screen import *
import os
display = Screen(BLACK)
bounce = display.draw_rectangle(10, 10, 100, 100, ORANGE)

velocity = 5
while display.playing_game():

	display.move(bounce, [0, velocity])
	if (display.get_position(bounce).y > 480):
		velocity = -5
	elif (display.get_position(bounce).y < 0):
		velocity = 5
	display.forward()
