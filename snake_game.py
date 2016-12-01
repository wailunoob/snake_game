import pygame, sys
import game_functions as gf
import game_settings
from snake import Snake
from tail import Tail
from pygame.sprite import OrderedUpdates
from food import Food
import random
from pygame.sprite import GroupSingle
from play_button import Play_button
from end_game_screen import EndGameScreen

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
	button = Play_button(screen, settings, "Play")
	end_game_screen = EndGameScreen(screen, settings, "Game Over")
	
	while True:
		screen.fill(settings.bg_color)
		gf.check_events(snake, food, screen, my_tail, tails, settings, button, gf, end_game_screen)
		if settings.game_active == False:
			button.draw_me()
		if settings.game_active == True:
			snake.update()	
			tails.update()
			snake.draw_me()
			food.update()
			pygame.time.wait(100)
		pygame.display.flip()

run_game()
