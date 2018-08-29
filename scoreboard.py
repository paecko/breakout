import pygame.font

class Scoreboard():

    def __init__(self,screen,gs):
        self.gs = gs
        self.screen = screen
        self.screen_rect = self.screen.get_rect()


        self.text_color=(0,0,0)
        self.font = pygame.font.SysFont(None,35)
        self.create_score()
        self.update_balls()


        self.update_level()
        #self.display_level()

    #Setting up score message
    def create_score(self):
        formatted_score = "{:,}".format(self.gs.score)
        self.msg_image = self.font.render("Score: " + formatted_score,True, self.text_color, self.gs.background_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.top = self.screen_rect.top
        self.msg_rect.right = self.screen_rect.right - 50

    #Setting up balls left message
    def update_balls(self):
        formatted_balls = "{:,}".format(self.gs.balls_left)
        self.msg_image_ball = self.font.render("Lives left: " + formatted_balls,True, self.text_color, self.gs.background_color)
        self.msg_rect_ball = self.msg_image_ball.get_rect()
        self.msg_rect_ball.top = self.screen_rect.top
        self.msg_rect_ball.left = self.screen_rect.left + 50

    #Setting up level message
    def update_level(self):
        formatted_level = "{:,}".format(self.gs.level)
        self.msg_image_level = self.font.render("Level: " + formatted_level, True, self.text_color, self.gs.background_color)
        self.msg_rect_level = self.msg_image_level.get_rect()
        self.msg_rect_level.center = self.screen_rect.center
        self.msg_rect_level.top = self.screen_rect.top
    """
    def display_level(self):
        #For displaying "get ready for next level"
        formatted_level = "{:,}".format(self.gs.level)
        self.level_display_image = self.font.render("Get ready for level: " + formatted_level, True, self.text_color, self.gs.background_color)
        self.level_display_rect = self.level_display_image.get_rect()
        self.level_display_rect.center = self.screen_rect.center
"""

    #Draws it all to screen
    def draw_stats(self):
        self.screen.blit(self.msg_image, self.msg_rect)
        self.screen.blit(self.msg_image_ball, self.msg_rect_ball)
        self.screen.blit(self.msg_image_level,self.msg_rect_level)

""""
    def draw_level(self):
        self.screen.blit(self.level_display_image, self.level_display_rect)
    """