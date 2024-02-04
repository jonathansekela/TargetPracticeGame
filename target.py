#!/usr/bin/env python

import pygame as pg
import load_functions as lf
import random

class Target(pg.sprite.Sprite):
	def __init__(self, img, directory):
		pg.sprite.Sprite.__init__(self)  # call Sprite initializer
		random.seed()
		self.image, self.rect = lf.load_image(img, directory, -1, 2)
		screen = pg.display.get_surface()
		self.area = screen.get_rect()
		self.rect.topleft = 10, 90
		self.move = 18
		self.hit = False
		self.current_time = pg.time.get_ticks()
		self.last_update = pg.time.get_ticks()
		self.__set_action_change_time_random()

	def __set_action_change_time_random(self):
		self.action_change_time = random.randint(1, 2) * 500 # .5 second intervals

	def update(self):
		# move or break, depending on target's state
		if self.hit:
			self._break()
		else:
			# self._walk()
			self._appear()

	def _walk(self):
		# move the target across the screen, and turn at the ends
		newpos = self.rect.move((self.move, 0))
		if not self.area.contains(newpos):
			if self.rect.left < self.area.left or self.rect.right > self.area.right:
				self.move = -self.move
				newpos = self.rect.move((self.move, 0))
				self.image = pg.transform.flip(self.image, True, False)
		self.rect = newpos

	def _appear(self):
		#need random x, y coordinate in screen width and height
		self.current_time = pg.time.get_ticks()
		if self.current_time - self.last_update >= self.action_change_time:
			self.rect.x = random.randint(0, self.area.right - self.rect.width)
			self.rect.y = random.randint(0, self.area.bottom - self.rect.height)
			self.last_update = self.current_time
			self.__set_action_change_time_random()

	def _break(self):
		# spin the target image
		center = self.rect.center
		self.hit = self.hit + 12
		if self.hit >= 360:
			self.hit = False
			self.image = self.original
		else:
			rotate = pg.transform.rotate
			self.image = rotate(self.original, self.hit)
		self.rect = self.image.get_rect(center=center)

	def shot(self):
		# this will cause the target to start spinning
		if not self.hit:
			self.hit = True
			self.original = self.image