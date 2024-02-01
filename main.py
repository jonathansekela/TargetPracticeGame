#!/usr/bin/env python

import pygame as pg
from pygame import mixer
import random

import gun
import target

pg.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pg.init()

# region general setup

SCREEN_WIDTH = 928
SCREEN_HEIGHT = 793

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Target Practice')
random.seed()

game_running = True
menu_running = True
# endregion

# region font setup
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
yellow = (255, 255, 0)

sans_bold_font = pg.font.Font('fonts/Pixeloid/TrueType (.ttf)/PixeloidSans-Bold.ttf', 32)
title_text = sans_bold_font.render('Shoot the targets as they appear!', True, green, black)
title_text_rect = title_text.get_rect()
title_text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20)

sans_font = pg.font.Font('fonts/Pixeloid/TrueType (.ttf)/PixeloidSans.ttf', 32)
sans_text = sans_font.render('Good General Font', True, green, black)
sans_text_rect = sans_text.get_rect()
sans_text_rect.center = (500, 250)
# endregion

# region game loop
while game_running:
	# update background
	screen.fill((0, 0, 0))

	"""bold and good for title stuff"""
	screen.blit(title_text, title_text_rect)
	
	# event handler
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_running = False
	
	pg.display.update()
# endregion

pg.quit()