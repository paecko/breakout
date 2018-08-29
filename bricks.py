import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
	
	def __init__(self,gs,color,x,y):
		super(Brick,self).__init__()
		
		self.image = pygame.Surface([gs.brick_width,gs.brick_length])
		self.image.fill(color)
		self.rect = self.image.get_rect()

		
		self.rect.x = x
		self.rect.y = y
		
		
