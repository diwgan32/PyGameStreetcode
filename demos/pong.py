import sys
sys.path.insert(0, '../core')
from Screen import *

game = Screen(BLUE)

# Setup player controled paddles
paddle_left = game.draw_rectangle(10, 200, 10, 80, WHITE)
paddle_right = game.draw_rectangle(620, 200, 10, 80, WHITE)

# Setup top and bottom borders
border_top = game.draw_rectangle(0, 0, 640, 3, RED)
border_bottom = game.draw_rectangle(0, 476, 640, 3, RED)

# Setup ball
ball = game.draw_circle(320, 240, 10, WHITE)
ball.set_velocity([-4, 1])

# Setup score counters
left_score = 0
right_score = 0
left_text = game.draw_text(100, 30, 'Left: 0', WHITE)
right_text = game.draw_text(450, 30, 'Right: 0', WHITE)

while game.playing_game():
    # Move the Left Paddle with W and S
    if paddle_left.y() > 0 and game.w_is_down():
        paddle_left.move([0,-7])
    if paddle_left.y() < 480 and game.s_is_down():
        paddle_left.move([0,7])

    # Move the Right Paddle with I and K
    if paddle_right.y() > 0 and game.i_is_down():
        paddle_right.move([0,-7])
    if paddle_right.y() < 480 and game.k_is_down():
        paddle_right.move([0,7])

    # Check if ball hits one of the paddles
    if game.collided_with(ball, paddle_left):
        vel = ball.get_velocity()
        ball.set_velocity([-vel.x, vel.y])
    if game.collided_with(ball, paddle_right):
        vel = ball.get_velocity()
        ball.set_velocity([-vel.x, vel.y])

    # Check if ball hits one of the borders
    if game.collided_with(ball, border_top):
        vel = ball.get_velocity()
        ball.set_velocity([vel.x, -vel.y])
    if game.collided_with(ball, border_bottom):
        vel = ball.get_velocity()
        ball.set_velocity([vel.x, -vel.y])

    # Check if one player scores
    if ball.x() < 0:
        right_score += 1
        right_text.set_text('Right: ' + str(right_score))
        ball.set_position([25, paddle_left.y()])
        ball.set_velocity([5, -2])

    if ball.x() > 640:
        left_score += 1
        left_text.set_text('Left: ' + str(left_score))
        ball.set_position([640-25, paddle_right.y()])
        ball.set_velocity([-5, -2])

    # Press q to quit game
    if game.q_is_down():
        game.quit()

    # Advance the game state
    game.forward()
