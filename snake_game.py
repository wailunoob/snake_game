import pygame, sys
import game_functions as gf
import game_settings
from snake import Snake
from tail import Tail
from pygame.sprite import OrderedUpdates
from food import Food
import random
from pygame.sprite import GroupSingle

def run_game():
	pygame.init()
	settings = game_settings.Settings()
	screen = pygame.display.set_mode(settings.resolution)
	snake = Snake(screen, settings)
	pygame.display.set_caption("Snake")
	my_tail = []
	x, y = gf.generate_randoms()
	food = GroupSingle(Food(snake, screen, x, y))
	tails = OrderedUpdates()
	gf.initialise_snake(snake, screen, my_tail, tails, settings)

	while True:
		gf.check_events(snake, food, screen, my_tail, tails, settings)
		screen.fill(settings.bg_color)
		snake.update()	
		tails.update()
		snake.draw_me()
		food.update()
		pygame.time.wait(100)
		pygame.display.flip()

run_game()