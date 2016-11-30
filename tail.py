from pygame.sprite import Sprite
import pygame

class Tail(Sprite):
	def __init__(self, snake, screen, number, my_tail):
		super().__init__()
		self.rect = pygame.Rect(0, 0, 30, 30)
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx - 15
		self.rect.centery = self.screen_rect.centery - 15
		self.color = (255, 0, 60)
		self.snake = snake
		self.number = number
		self.old_position = pygame.Rect(self.rect.x, self.rect.y, 30, 30)
		self.my_tail = my_tail
		self.initialise_tail()
	
	def update(self):
		if self.number == 1:
			self.old_position = self.rect.copy()
			self.rect.x = self.snake.old_position.x
			self.rect.y = self.snake.old_position.y
			pygame.draw.rect(self.screen, self.color, self.rect)
		elif self.number > 1:
			self.old_position = self.rect.copy()
			self.rect.x = self.tail_before.old_position.x
			self.rect.y = self.tail_before.old_position.y
			pygame.draw.rect(self.screen, self.color, self.rect)
	
	def initialise_tail(self):
		if self.number == 1:
			pass
		elif self.number > 1:
			self.tail_before = self.my_tail[self.number - 2]

