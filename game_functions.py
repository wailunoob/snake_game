import sys, pygame
from tail import Tail
import random
from food import Food
from pygame.sprite import OrderedUpdates

def check_events(snake, food, screen, my_tail, tails, settings, button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				sys.exit()
		check_keydown_events(event, snake, button, settings)
	if pygame.sprite.collide_rect(snake, food.sprite):
		x, y = generate_randoms()
		food.add(Food(snake, screen, x, y))
		settings.snake_length += 1
		tail_sprite = Tail(snake, screen, settings.snake_length - 2, my_tail)
		my_tail.append(tail_sprite)
		for body in my_tail:
			tails.add(body)

def check_keydown_events(event, snake, button, settings):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_DOWN and snake.moving_up == False:
			snake.moving_down = True
			snake.moving_up = False
			snake.moving_left = False
			snake.moving_right = False
		if event.key == pygame.K_UP and snake.moving_down == False:
			snake.moving_down = False
			snake.moving_up = True
			snake.moving_left = False
			snake.moving_right = False
		if event.key == pygame.K_LEFT and snake.moving_right == False:
			snake.moving_down = False
			snake.moving_up = False
			snake.moving_left = True
			snake.moving_right = False
		if event.key == pygame.K_RIGHT and snake.moving_left == False:
			snake.moving_down = False
			snake.moving_up = False
			snake.moving_left = False
			snake.moving_right = True
	if event.type == pygame.MOUSEBUTTONDOWN:
		x, y = pygame.mouse.get_pos()
		print(x, y, button.rect.collidepoint(x, y), settings.game_active) #!!!
		if button.rect.collidepoint(x, y) == True:
			settings.game_active = True


def initialise_snake(snake, screen, my_tail, tails, settings):
	for number in range(1, settings.snake_length):
		tail_sprite = Tail(snake, screen, number, my_tail)
		my_tail.append(tail_sprite)
		for body in my_tail:
			tails.add(body)

def generate_randoms():
	x = random.randrange(0, 1200, 30)
	y = random.randrange(0, 900, 30)
	return x, y
