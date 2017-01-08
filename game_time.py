import pygame

class GTime():
	def __init__(self, clock):
		self.time = 0
		self.clock = clock

	def update(self):
		if self.clock.get_time() < 200:
			self.time += self.clock.get_time()
