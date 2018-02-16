"""
Test the library in Screen.py
"""
import sys
sys.path.insert(0, '../core')
from Screen import *

display = Screen(BLACK)

bounce = display.draw_circle(50, 50, 20, ORANGE)
wall = display.draw_rectangle(0, 460, 640, 20, BLUE)

velocity = 5
while display.playing_game():

	bounce.move([0, velocity])
	if (bounce.get_position().y > 480):
		velocity = -5
	elif (bounce.get_position().y < 0):
		velocity = 5
	if (display.collided_with(bounce, wall)):
		velocity *= -1
	display.forward()
