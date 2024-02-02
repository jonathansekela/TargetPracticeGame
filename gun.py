#!/usr/bin/env python

import pygame as pg
import load_functions as lf

class Gun(pg.sprite.Sprite):
	# moves a targeting reticle on the screen, following the mouse

	def __init__(self, img, directory):
		pg.sprite.Sprite.__init__(self)  # call sprite initializer
		self.image, self.rect = lf.load_image(img, directory, -1)
		self.fist_offset = (0, 0)
		self.shooting = False

	def update(self):
		# move the reticle based on the mouse position
		pos = pg.mouse.get_pos()
		self.rect.center = pos
		self.rect.move_ip(self.fist_offset)
		# if self.shooting:
		# 	self.rect.move_ip(15, 25)

	def shoot(self, target):
		# returns true if the reticle collides with the target
		if not self.shooting:
			self.shooting = True
			hitbox = self.rect.inflate(-5, -5)
			return hitbox.colliderect(target.rect)

	def unshoot(self):
		# called to reset the gun
		self.shooting = False