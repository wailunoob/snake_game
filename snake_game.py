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
from score import Score
from game_time import GTime

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
	score = Score(screen, settings)
	clock = pygame.time.Clock()
	gametime = GTime(clock)
	
	while True:
		screen.fill(settings.bg_color)
		score.draw_me()
		gf.check_events(snake, food, screen, my_tail, tails, settings, button, gf, end_game_screen, score, gametime)
		if settings.game_active == False:
			if gf.lose_condition_met(snake, settings, tails, gametime) == False:
				button.draw_me()
		if settings.game_active == True:
			snake.update()	
			tails.update()
			snake.draw_me()
			food.update()
			clock.tick(10)
			gametime.update()
			if gametime.update():
				gametime.keypressed = False
			print(gametime.time)
		pygame.display.flip()

run_game()
