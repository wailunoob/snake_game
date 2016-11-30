import pygame
from pygame.sprite import Sprite
import random

class Food(Sprite):
	def __init__(self, snake, screen, x, y):
		super().__init__()
		self.snake = snake
		self.screen = screen
		self.rect = pygame.Rect(0, 0, 30, 30)
		self.color = (0, 0, 0)
		self.rect.x = x
		self.rect.y = y
	
	def update(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
