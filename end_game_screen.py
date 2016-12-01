import pygame
import pygame.font

class EndGameScreen():
	def __init__(self, screen, settings, msg):
		self.rect = pygame.Rect(0, 0, 200, 50)
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.msg = msg
		self.rect.center = self.screen_rect.center
		self.font = pygame.font.SysFont(None, 48)
		self.prep_msg()
	
	def prep_msg(self):
		self.msg_image = self.font.render(
		self.msg, True, self.settings.bg_color, self.settings.snake_color
		)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.screen_rect.center
	
	def draw_me(self):
		pygame.draw.rect(self.screen, self.settings.snake_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
