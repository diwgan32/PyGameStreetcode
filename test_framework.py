"""
Test the library in Screen.py
"""
from Screen import *

display = Screen(BLACK)

while 1:            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

    
    pygame.draw.rect(display.screen, (34, 34, 34), pygame.Rect(300,350,100,100))

    pygame.display.flip()
    display.forward()