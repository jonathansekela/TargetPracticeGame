#!/usr/bin/env python

import pygame as pg
import os

def load_image(name, directory, colorkey=None, scale=1):
	fullname = os.path.join(directory, name)
	image = pg.image.load(fullname)
	image = image.convert()

	size = image.get_size()
	size = (size[0] * scale, size[1] * scale)
	image = pg.transform.scale(image, size)

	if colorkey is not None:
		if colorkey == -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey, pg.RLEACCEL)
	return image, image.get_rect()

def load_sound(name, directory):
	class NoneSound:
		def play(self):
			pass

	if not pg.mixer or not pg.mixer.get_init():
		return NoneSound()

	fullname = os.path.join(directory, name)
	sound = pg.mixer.Sound(fullname)

	return sound