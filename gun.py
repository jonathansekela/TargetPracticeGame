#!/usr/bin/env python

import pygame as pg
import os

import load_functions as lf

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data") # @todo: change this to work

class Gun(pg.sprite.Sprite):
	"""moves a clenched fist on the screen, following the mouse"""

	def __init__(self):
		pg.sprite.Sprite.__init__(self)  # call Sprite initializer
		self.image, self.rect = lf.load_image("fist.png", data_dir, -1)
		self.fist_offset = (-235, -80)
		self.punching = False

	def update(self):
		"""move the fist based on the mouse position"""
		pos = pg.mouse.get_pos()
		self.rect.topleft = pos
		self.rect.move_ip(self.fist_offset)
		if self.punching:
			self.rect.move_ip(15, 25)

	def shoot(self, target):
		"""returns true if the reticle collides with the target"""
		if not self.punching:
			self.punching = True
			hitbox = self.rect.inflate(-5, -5)
			return hitbox.colliderect(target.rect)

	def unshoot(self):
		"""called to reset the gun"""
		self.punching = False