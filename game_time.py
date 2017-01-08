import pygame

class GTime():
	def __init__(self, clock):
		self.time = 0
		self.keypressed = False
		self.clock = clock

	def update(self):
		if self.clock.get_time() < 110:
			self.time += 100
		self.keypressed = False
