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

mono_font = pg.font.Font('fonts/Pixeloid/TrueType (.ttf)/PixeloidMono.ttf', 32)
mono_text = mono_font.render('mono: It\'s Yaboi Big Chungus', True, green, black)
mono_text_rect = mono_text.get_rect()
mono_text_rect.center = (500, 200)

sans_font = pg.font.Font('fonts/Pixeloid/TrueType (.ttf)/PixeloidSans.ttf', 32)
sans_text = sans_font.render('sans: It\'s Yaboi Big Chungus', True, green, black)
sans_text_rect = sans_text.get_rect()
sans_text_rect.center = (500, 250)

sans_bold_font = pg.font.Font('fonts/Pixeloid/TrueType (.ttf)/PixeloidSans-Bold.ttf', 32)
sans_bold_text = sans_bold_font.render('sans bold: It\'s Yaboi Big Chungus', True, green, black)
sans_bold_text_rect = sans_bold_text.get_rect()
sans_bold_text_rect.center = (400, 300)

zerocool_font = pg.font.Font('fonts/ZeroCool/zeroCool.ttf', 32)
zerocool_text = zerocool_font.render('ZeroCool: It\'s Yaboi Big Chungus', True, yellow, black)
zerocool_text_rect = zerocool_text.get_rect()
zerocool_text_rect.center = (500, 350)
# endregion

# region game loop
while game_running:
	# update background
	screen.fill((0, 0, 0))
	
	"""not my favorite. Too computer-ey and hard to read quickly."""
	screen.blit(mono_text, mono_text_rect)
	
	"""this one is good. gamey and readable."""
	screen.blit(sans_text, sans_text_rect)
	
	"""bold and good for title stuff"""
	screen.blit(sans_bold_text, sans_bold_text_rect)
	
	"""spooky. not really 'cool', just vaguely threatening and wonky."""
	screen.blit(zerocool_text, zerocool_text_rect)
	
	# event handler
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_running = False
	
	pg.display.update()
# endregion

pg.quit()