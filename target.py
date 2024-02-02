#!/usr/bin/env python

import pygame as pg
import load_functions as lf

class Target(pg.sprite.Sprite):
	def __init__(self, img, directory):
		pg.sprite.Sprite.__init__(self)  # call Sprite initializer
		self.image, self.rect = lf.load_image(img, directory, -1, 2)
		screen = pg.display.get_surface()
		self.area = screen.get_rect()
		self.rect.topleft = 10, 90
		self.move = 18
		self.hit = False

	def update(self):
		# move or break, depending on target's state
		if self.hit:
			self._break()
		else:
			self._walk()

	def _walk(self):
		# move the target across the screen, and turn at the ends
		newpos = self.rect.move((self.move, 0))
		if not self.area.contains(newpos):
			if self.rect.left < self.area.left or self.rect.right > self.area.right:
				self.move = -self.move
				newpos = self.rect.move((self.move, 0))
				self.image = pg.transform.flip(self.image, True, False)
		self.rect = newpos

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