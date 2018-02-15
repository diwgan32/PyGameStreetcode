"""
    Test the library in Screen.py
    """
from Screen import *
import os
display = Screen(BLACK)
my_shape = display.draw_rectangle(100, 100, 100, 100, ORANGE)
apple = []
print apple
apple.append(99)
apple.append(199)
apple.append(299)
print (apple)
for number in apple:
    print (number + 99)
for number in apple:
    print (number + 299)
shapes = []
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
        chillys = display.draw_rectangle(display.get_position(my_shape).x, (display.get_position(my_shape).y), 95, 30, RED)
        display.move(chillys,[85,0])
        shapes.append(chillys)
        for bullet in shapes:
            display.move(bullet,[5,0])
        
     
    display.forward()
