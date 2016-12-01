import pygame
import pygame.font

class Score():
	def __init__(self, screen, settings):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.settings = settings
		self.score = 0
		self.font = pygame.font.SysFont(None, 48)

	def draw_me(self):
		self.msg_image = self.font.render(
		str(self.score), True, self.settings.snake_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.top = self.screen_rect.top
		self.msg_image_rect.right = self.screen_rect.right - 5
		self.screen.blit(self.msg_image, self.msg_image_rect)

	
	def increase_score(self):
		self.score += 100
