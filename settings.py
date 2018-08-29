import math
class Settings():

    def __init__(self):

        #Game active or not


        #Screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.background_color = (105,105,105)

        #paddle settings
        self.paddle_speed = 0.5

        #self.paddle_width = 600  //when paddle was a rect, now a image
        #self.paddle_length = 15
        #self.paddle_color = (0, 0, 255)

        #Ball settings
        self.ball_color = (0,0,255)
        self.start_x = int(self.screen_width/2)
        self.start_y = int(self.screen_height/2)
        self.ball_speed_x_holder = 0.5
        self.ball_speed_x = self.ball_speed_x_holder
        self.ball_speed_y = 0.7
        self.speed_factor = 0.3
        self.maxbounceangle = (5*math.pi)/12
        self.total_balls = 99
        self.balls_left = self.total_balls


        # BRICK WIDTH AND LENGTH
        self.brick_width = 60
        self.brick_length = 25

        self.marginx = 5
        self.marginx2 = 100

        #dunno why this works
        self.marginy_holder = 40
        self.marginy = self.marginy_holder

        #Marginy y for other levels
        self.marginy2 = 40



        self.blue = (0,0,255)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.yellow = (204,204,0)
        self.purple = (128,0,128)
        self.orange = (255,165,0)
        self.black = (0,0,0)
        self.pink = (255,192,203)
        self.silver = (192,192,192)
        self.colors = [self.red,self.blue,self.orange,self.green,self.silver,self.yellow,self.pink,self.black,self.purple,self.red]

        self.score_holder = 0
        self.score = self.score_holder


        #Becomes True when balls run out, stop game and displays play button
        self.game_active = False

        #If game over sound plays or not
        self.play_sound = True
        self.level_holder = 1
        self.level = self.level_holder

        self.first_start = False