import pygame

class Snake(pygame.sprite.Sprite):
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, 30, 30)
		self.screen_rect = self.screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx - 15
		self.rect.centery = self.screen_rect.centery - 15
		self.settings = settings
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		self.old_position = pygame.Rect(self.rect.x, self.rect.y, 30, 30)
	
	def draw_me(self):
		pygame.draw.rect(self.screen, self.settings.snake_color, 
			self.rect)
	
	def update(self):
		if self.moving_left == True:
			self.old_position = self.rect.copy()
			self.rect.x -= 30
		elif self.moving_right == True:
			self.old_position = self.rect.copy()
			self.rect.x += 30
		elif self.moving_up == True:
			self.old_position = self.rect.copy()
			self.rect.y -= 30
		elif self.moving_down == True:
			self.old_position = self.rect.copy()
			self.rect.y += 30
