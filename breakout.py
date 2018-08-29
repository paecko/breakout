import pygame
import sys
from settings import Settings
from paddle import Paddle
from ball import Ball
from bricks import Brick
from pygame.sprite import Group
from play_button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    # get settings and set up screen
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width,gs.screen_height))
    screen_rect = screen.get_rect()  # get dimensions of screen
    # following initializes Play Button, score label, paddle, ball and bricks
    play_button = Button(screen, "Play")
    scoreboard = Scoreboard(screen, gs)
    paddle = Paddle(screen, gs)
    # bricks in pygame container class 'Group' to manage all brick sprites as one unit.
    bricks = Group()
    # also maintain ball in a group, since it makes it easier to restart game with new ball when user loses. also
    # makes detecting collision between bricks and ball simpler.
    balls = Group(Ball(screen, gs, paddle))

    def check_brick_collision():
        # returns dict of brick sprites that collide with ball. 3rd and 4th parameters are for deleting the collided sprites
        collisions = pygame.sprite.groupcollide(balls, bricks, False, True)

        # if collisions is not None (no collision)
        if collisions:
            # get the center x-coord of the ball
            for ball in balls:
                ball_center_rect = ball.rect.centerx
            for value in collisions.values():
                for brick in value:
                    intersection = brick.rect.centerx - ball_center_rect
                    normalized = (intersection/(gs.brick_width/2))

            effect = pygame.mixer.Sound('sounds/pong1.wav')
            effect.play()
            gs.ball_speed_y = abs(gs.ball_speed_y)
            gs.ball_speed_x = normalized
            gs.score += 5
            scoreboard.create_score()

    def update_ball():
        balls.update()
        check_brick_collision()
        for ball in balls.copy():
            # if ball is not present on screen and game is over, have to reset ball settings
            if ball.rect.top >= gs.screen_height and gs.game_over:
                balls.remove(ball)
                gs.balls_left -= 1
                # Reset ball speed
                gs.ball_speed_x = gs.ball_speed_x_holder
                # To prevent game over sound and ball down sound from playing at same time since
                if gs.balls_left > 1:
                    effect = pygame.mixer.Sound('sounds/ball_down.wav')
                    effect.play()
                # Updates text of lives left
                scoreboard.update_balls()
                new_ball = Ball(screen, gs, paddle)
                balls.add(new_ball)

    #Level1 (4x9)
    def setup_bricks():
        # each row will have 9 bricks
        for row in range(4):
            for column in range(0, 9):
                # create new brick
                brick = Brick(gs, gs.colors[row], column * (gs.brick_width+gs.marginx)+12, gs.marginy)
                bricks.add(brick)

            # update y marin as next row will be placed down
            gs.marginy += gs.brick_length + 5

    # Level2 (8x4)
    def setup_bricks2():
        for row in range(8):
            for column in range(4):
                brick = Brick(gs, gs.colors[row], column * (gs.brick_width+gs.marginx2)+40, gs.marginy)
                bricks.add(brick)
            gs.marginy += gs.brick_length + 5

    # Level3  (6x5)
    def setup_bricks3():
        for row in range(6):
            for column in range(5):
                brick = Brick(gs, gs.colors[row], column * (gs.brick_width*2) + 40, gs.marginy2)
                bricks.add(brick)
            gs.marginy2 += gs.brick_length * 2
        gs.marginy2 = gs.marginy_holder

        for row in range(5):
            for column in range(4):
                brick = Brick(gs, gs.colors[row], column * (gs.brick_width*2) + 40 + gs.brick_width, gs.marginy2 + gs.brick_length)
                bricks.add(brick)
            gs.marginy2 += gs.brick_length*2
        gs.marginy2 = gs.marginy_holder


    def setup_bricks4():
        for row in range(0):
            for column in range(0):
                brick = Brick(gs,gs.colors[row], column*(gs.brick_width + gs.marginx)+50 + gs.brick_width,gs.brick_length*3 + gs.marginy)
                bricks.add(brick)
            gs.marginy += gs.brick_length + 5
        gs.marginy = gs.marginy_holder

        for row in range(0):
            for column in range(0):
                brick = Brick(gs,gs.colors[row],(screen_rect.centerx),gs.brick_length + gs.marginy)
                bricks.add(brick)
            gs.marginy += gs.brick_length+5
        gs.marginy = gs.marginy_holder

        for row in range(0):
            for column in range(0):
                brick = Brick(gs, gs.colors[row], gs.screen_width - column * (gs.brick_width - gs.marginx) - 50 -gs.brick_width,gs.brick_length * 3 + gs.marginy)
                bricks.add(brick)
            gs.marginy += gs.brick_length + 5
        gs.marginy = gs.marginy_holder

    def change_level():
        # run the setup_bricks corresponding to the level
        eval('setup_bricks' + str(gs.level))

    # Checks for paddle movement input(arrow keys) and resets game from input when game has ended.
    def reset():
        setup_bricks()
        #Resetting marginy so it does not draw lower
        gs.marginy = gs.marginy_holder
        #Update level, score and reset speed
        scoreboard.update_level()
        gs.level = gs.level_holder
        gs.score = gs.score_holder
        scoreboard.create_score()
        gs.ball_speed_x = gs.ball_speed_x_holder
        gs.game_over = True
        gs.balls_left = gs.total_balls
        gs.play_sound = True

    def check_events():
        # Quits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and gs.game_over:
                    paddle.paddle_moving_right = True
                elif event.key == pygame.K_LEFT and gs.game_over:
                    paddle.paddle_moving_left = True
                # Reset game input
                elif event.key == pygame.K_SPACE and not gs.game_over:
                    gs.game_over = True
                    reset()
                # Exit game
                elif event.key == pygame.K_q:
                    sys.exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    paddle.paddle_moving_right = False
                elif event.key == pygame.K_LEFT:
                    paddle.paddle_moving_left = False

            if event.type == pygame.MOUSEBUTTONDOWN and not gs.game_over:
                mousex, mousey = pygame.mouse.get_pos()
                button_clicked = play_button.rect.collidepoint(mousex, mousey)
                if button_clicked:
                    gs.game_over = True
                    reset()
    #Game loop
    while True:
        check_events()
        #Updates
        if gs.game_over:
            update_ball()
            paddle.update_paddle()
        #drawing
        screen.fill(gs.background_color)
        if not gs.game_over:
            play_button.draw_buttons()
        paddle.draw_paddle()
        bricks.draw(screen)
        for ball in balls.sprites():
            ball.draw_ball()
        scoreboard.draw_stats()
        pygame.display.update()

        #When balls run out, display play button
        if gs.balls_left == 0:
            if gs.play_sound:
                effect = pygame.mixer.Sound('sounds/game_over.wav')
                effect.play()
                gs.play_sound = False
                bricks.empty()



            gs.game_over = False
            gs.first_start = True
            check_events()
            scoreboard.update_balls()
        #Goes to next level
        elif len(bricks) == 0 and not gs.balls_left == 0:
            balls.empty()
            new_ball = Ball(screen, gs, paddle)
            balls.add(new_ball)
            change_level()
            #Not completely sure why this works and why draw_stats() doesnt keep updating gs.level
            scoreboard.update_level()
            pygame.time.delay(1000)
            #FIGURE OUT HOW TO CENTER PADDLE
            gs.level += 1


if __name__ == '__main__':
    run_game()
