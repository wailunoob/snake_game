import pygame

class Play_button():
	def __init__(self, screen, settings):
		self.rect = pygame.Rect(0, 0, 200, 50)
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.settings = settings
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
	
	def draw_me(self):
		pygame.draw.rect(self.screen, self.settings.snake_color, self.rect)
