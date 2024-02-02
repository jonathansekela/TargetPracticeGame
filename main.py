#!/usr/bin/env python

import pygame as pg
from pygame import mixer
import random

import gun
import target
import load_functions as lf

pg.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pg.init()

# region general setup

SCREEN_WIDTH = 928
SCREEN_HEIGHT = 793

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Target Practice')
random.seed()

# load music
pg.mixer.music.load('Music/Of Far Different Nature - 0 to 100 (CC-BY).ogg')
pg.mixer.music.set_volume(.5)  # 50% original volume
pg.mixer.music.play(-1, 0.0, 5000)

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
title_text = sans_bold_font.render('SHOOT THE TARGETS AS THEY APPEAR', True, green, black)
title_text_rect = title_text.get_rect()
title_text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20)

sans_font = pg.font.Font('fonts/Pixeloid/TrueType (.ttf)/PixeloidSans.ttf', 32)
sans_text = sans_font.render('Good General Font', True, green, black)
sans_text_rect = sans_text.get_rect()
sans_text_rect.center = (500, 250)
# endregion

shoot_sound = lf.load_sound("556 Single Isolated.mp3", "sfx/556 Gunshots")

gune = gun.Gun("1.png", "sprites/green crosshairs")
targ = target.Target("168.png", "sprites/red crosshairs")
allsprites = pg.sprite.RenderPlain((targ, gune))

clock = pg.time.Clock()

# region game loop
while game_running:
	clock.tick(60)
	# update background
	screen.fill((0, 0, 0))

	screen.blit(title_text, title_text_rect)
	
	# event handler
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_running = False
		elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
			game_running = False
		elif event.type == pg.MOUSEBUTTONDOWN:
			shoot_sound.play()
			if gune.shoot(targ):
				targ.shot()
		elif event.type == pg.MOUSEBUTTONUP:
			gune.unshoot()

		allsprites.update()

		# Draw Everything
		allsprites.draw(screen)
		pg.display.flip()
	
	pg.display.update()
# endregion

pg.quit()