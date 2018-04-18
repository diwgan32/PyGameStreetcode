"""
Test the library in Screen.py
"""
import sys
sys.path.insert(0, '../core')
from Screen import *

# Setup game object
game = Screen(WHITE, title='Use Arrowkeys to move the plane')
keyboard = game.get_keyboard()

# Load Images
plane = game.draw_image(320, 240, 'PlayerPlane/plane1_down.gif')

while game.playing_game():

    # Steer plane woth arrow keys
    if keyboard.up_is_down():
        plane.move([0,-2])
        plane.set_image('PlayerPlane/plane1_up.gif')
    if keyboard.down_is_down():
        plane.move([0,2])
        plane.set_image('PlayerPlane/plane1_down.gif')
    if keyboard.left_is_down():
        plane.move([-2,0])
        plane.set_image('PlayerPlane/plane1_left.gif')
    if keyboard.right_is_down():
        plane.move([2,0])
        plane.set_image('PlayerPlane/plane1_right.gif')

    # Press q to quit game
    if keyboard.q_is_down():
        game.quit()

    # Advance game state
    game.forward()
