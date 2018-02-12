"""
    Test the library in Screen.py
    """
from Screen import *
import os
display = Screen(BLACK)
while display.playing_game():
    
    display.forward()
