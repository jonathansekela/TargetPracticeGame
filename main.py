#!/usr/bin/env python
import pygame as pg
from pygame import mixer
import random

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

# region game loop
while game_running:
	# update background
	screen.fill((0, 0, 0))
	# screen.blit(BACKGROUND, (0, 0))
	
	# event handler
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_running = False
	
	pg.display.update()
# endregion

pg.quit()