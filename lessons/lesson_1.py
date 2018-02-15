"""
    Test the library in Screen.py
    """
import sys
sys.path.insert(0, '../core')
from Screen import *

display = Screen(BLACK)
while display.playing_game():
    
    display.forward()
