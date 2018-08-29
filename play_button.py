import pygame.font

class Button():
	def __init__(self,screen,msg):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		
		self.button_color = (200,200,200)
		self.text_color = (0,0,0)
		self.font =  pygame.font.SysFont(None,35)
		
		self.rect = pygame.Rect(0,0,100,50)
		self.rect.center = self.screen_rect.center
		self.create_message(msg)
	
	def create_message(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.center = self.screen_rect.center
		
	def draw_buttons(self):
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image, self.msg_rect)
		
