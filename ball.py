import pygame
from pygame.sprite import Sprite
import math
class Ball(Sprite):

    def __init__(self,screen,gs,paddle):
        super(Ball,self).__init__()
        self.gs = gs
        self.screen = screen
        self.paddle = paddle
        self.image =  pygame.image.load('images/ball.png').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.center = self.screen_rect.center

        self.temp_x = self.rect.centerx
        self.temp_y = self.rect.centery

    """def get_bounce_angle(self,surface_center, surface_size):

        surface_to_intersection = surface_center - self.rect.centerx
        normalized_intersection = surface_to_intersection/(surface_size/2)
        bounce_angle = normalized_intersection * self.gs.maxbounceangle
        return bounce_angle
        """

    def check_ball_collisions(self):

        #Screen collision
        if self.rect.right >= self.screen_rect.right:
            effect = pygame.mixer.Sound('sounds/pong3.wav')
            effect.play()
            self.gs.ball_speed_x  *= -1

        if self.rect.left <= self.screen_rect.left:
            effect = pygame.mixer.Sound('sounds/pong3.wav')
            effect.play()


            self.gs.ball_speed_x  *= -1

        if self.rect.top <= self.screen_rect.top:
            self.gs.ball_speed_y *=  -1

        #Paddle collision

        collisions = self.rect.colliderect(self.paddle.rect)
        if collisions and self.rect.right != self.paddle.rect.left and self.rect.left != self.paddle.rect.right:

                paddle_center = self.paddle.rect.centerx
                ball_center = self.rect.centerx

                intersection = paddle_center - ball_center
                normalized = (intersection/(self.paddle.rect.width/2))

                bounce_angle = normalized * self.gs.maxbounceangle

                self.gs.ball_speed_y = -abs(self.gs.ball_speed_y)
                self.gs.ball_speed_x = normalized


                effect = pygame.mixer.Sound('sounds/pong1.wav')
                effect.play()

    def update(self):

        self.check_ball_collisions()
        self.temp_x += self.gs.ball_speed_x * self.gs.speed_factor
        self.temp_y += self.gs.ball_speed_y * self.gs.speed_factor


        self.rect.centerx = self.temp_x
        self.rect.centery = self.temp_y


    def draw_ball(self):
        self.screen.blit(self.image,self.rect)



