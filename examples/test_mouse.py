"""
Test the library in Screen.py
"""
import sys
sys.path.insert(0, '../core')
from Screen import *

# Setup game object
game = Screen(WHITE, title='Click to shoot')
keyboard = game.get_keyboard()
mouse = game.get_mouse()

# Draw clickable shapes
box1 = game.draw_rectangle(100, 100, 300, 50, RED)
ball2 = game.draw_circle(300, 300, 40, ORANGE)

# Draw circle to follow mouse
ball1 = game.draw_circle(320, 240, 20, BLUE)

while game.playing_game():
    (mx, my) = mouse.get_position()
    ball1.set_position((mx, my))

    if mouse.ontop(box1):
        box1._color = BLUE
    else:
        box1._color = RED

    if mouse.ontop(ball2):
        ball2._color = RED
    else:
        ball2._color = ORANGE

    if mouse.left_is_pressed():
        bullet = game.draw_circle(mx, my, 3, BLACK)
        bullet.set_velocity((0, -2))

    # Press q to quit game
    if keyboard.q_is_down():
        game.quit()

    # Advance game state
    game.forward()
