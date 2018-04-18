"""
Test the library in Screen.py
"""
import sys
sys.path.insert(0, '../core')
from Screen import *

display = Screen(BLACK)
keyboard = display.get_keyboard()
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
new_shape = display.draw_rectangle(10, 100, 50, 100, BLUE)
circle = display.draw_circle(400, 200, 50, YELLOW)

projectiles = []
while display.playing_game():
    display.forward()
    if(keyboard.right_is_down()):
        my_shape.move([3, 0])
    if(keyboard.left_is_down()):
        my_shape.move([-3,0])
    if(keyboard.up_is_down()):
        my_shape.move([0, -3])
    if(keyboard.down_is_down()):
        my_shape.move([0, 3])
    if(keyboard.enter_is_down()):
        display.delete(my_shape)

    if(keyboard.space_is_pressed()):
        x = my_shape.get_position().x
        y = my_shape.get_position().y
        bullet = display.draw_circle(x, y, 5, RED)
        projectiles.append(bullet)

    if(keyboard.space_is_released()):
        x = my_shape.get_position().x
        y = my_shape.get_position().y
        bullet = display.draw_circle(x, y, 5, BLUE)
        projectiles.append(bullet)

    for bullet in projectiles:
        bullet.move([-10, 0])
        if(display.collided_with(bullet, new_shape)):
            display.delete(new_shape)
    if (display.collided_with(my_shape, new_shape) or display.collided_with(my_shape, circle)):
        my_shape.move([0, 0])
        

