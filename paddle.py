import pygame


class Paddle():
    def __init__(self,screen,gs):
        self.screen = screen
        self.gs = gs
        self.image = pygame.image.load('images/paddle2.png').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        self.paddle_speed = self.gs.paddle_speed

        self.paddle_moving_right = False
        self.paddle_moving_left = False
        self.x = float(self.rect.centerx)

    def update_paddle(self):
        if self.paddle_moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.paddle_speed
        if self.paddle_moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.paddle_speed
        self.rect.centerx = self.x


    def draw_paddle(self):
        self.screen.blit(self.image,self.rect)



    def center_paddle(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
