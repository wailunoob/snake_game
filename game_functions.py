import sys, pygame
from tail import Tail
import random
from food import Food
from pygame.sprite import OrderedUpdates

def check_events(snake, food, screen, my_tail, tails, settings, button, gf, end_game_screen, score, gametime):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				sys.exit()
		check_keydown_events(event, snake, button, settings, gametime)
	if pygame.sprite.collide_rect(snake, food.sprite):
		x, y = generate_randoms()
		food.add(Food(snake, screen, x, y))
		settings.snake_length += 1
		score.increase_score()
		tail_sprite = Tail(snake, screen, settings.snake_length - 1, my_tail)
		my_tail.append(tail_sprite)
		for body in my_tail:
			tails.add(body)
	if lose_condition_met(snake, settings, tails, gametime):
		settings.game_active = False
		end_game_screen.draw_me()


def check_keydown_events(event, snake, button, settings, gametime):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_DOWN and snake.moving_up == False and gametime.keypressed == False:
			print("key registered!")
			gametime.keypressed = True
			snake.moving_down = True
			snake.moving_up = False
			snake.moving_left = False
			snake.moving_right = False
		elif event.key == pygame.K_UP and snake.moving_down == False and gametime.keypressed == False:
			print("key registered!")
			gametime.keypressed = True
			snake.moving_down = False
			snake.moving_up = True
			snake.moving_left = False
			snake.moving_right = False
		elif event.key == pygame.K_LEFT and snake.moving_right == False and gametime.keypressed == False:
			print("key registered!")
			gametime.keypressed = True
			snake.moving_down = False
			snake.moving_up = False
			snake.moving_left = True
			snake.moving_right = False
		elif event.key == pygame.K_RIGHT and snake.moving_left == False and gametime.keypressed == False:
			print("key registered!")
			gametime.keypressed = True
			snake.moving_down = False
			snake.moving_up = False
			snake.moving_left = False
			snake.moving_right = True
	if event.type == pygame.MOUSEBUTTONDOWN:
		x, y = pygame.mouse.get_pos()
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

def lose_condition_met(snake, settings, tails, gametime):
	width, height = settings.resolution
	if snake.rect.centerx > width or snake.rect.centerx < 0:
		return True
	elif snake.rect.centery > height or snake.rect.centery < 0:
		return True
	elif pygame.sprite.spritecollide(snake, tails, False, pygame.sprite.collide_rect_ratio(0.5)) and gametime.time != 0:
			print(pygame.sprite.spritecollide(snake, tails, False, pygame.sprite.collide_rect_ratio(0.5)))
			return True
	else:
		return False
