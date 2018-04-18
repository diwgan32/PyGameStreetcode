"""
Test the library in Screen.py
"""
import sys
sys.path.insert(0, '../core')
from Screen import *

# Setup game object
game = Screen(WHITE)
keyboard = game.get_keyboard()

# Setup text objects
text_1 = game.draw_text(100, 100, "fast counter", BLACK, 'Comic Sans MS', 80)
text_2 = game.draw_text(100, 300, "slow counter", RED, 'Arial', 80)
text_3 = game.draw_text(100, 250, "This text is small and blue >>>", BLUE, 'Impact', 20)

# setup counters
counter_1 = 0
counter_2 = 0

while game.playing_game():
    # Update counters
    counter_1 = counter_1 + 1
    counter_2 = counter_2 + 0.07

    # Update text objects with new counters
    text_1.set_text('fast ' + str(counter_1))
    text_2.set_text('slow ' + str(int(counter_2)))

    # Move text_3 around
    text_3.move([0.5, 0])

    # Press q to quit game
    if keyboard.q_is_down():
        game.quit()

    # Advance game state
    game.forward()
