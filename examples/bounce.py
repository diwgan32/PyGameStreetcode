"""
Test the library in Screen.py
"""
import sys
sys.path.insert(0, '../core')
from Screen import *

display = Screen(BLACK)

bounce = display.draw_rectangle(10, 10, 100, 100, ORANGE)
wall = display.draw_rectangle(0, 460, 640, 20, BLUE)

velocity = 5
while display.playing_game():

	display.move(bounce, [0, velocity])
	if (display.get_position(bounce).y > 480):
		velocity = -5
	elif (display.get_position(bounce).y < 0):
		velocity = 5
	if (display.collided_with(bounce, wall)):
		velocity *= -1
	display.forward()
