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

# @todo: make it so the target doesn't always appear
# @todo: get backend together - sql and db

# region setup
GAME_ID = 2

# region screen setup
SCREEN_WIDTH = 928
SCREEN_HEIGHT = 793

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Target Practice')
random.seed()
# endregion

# region load music
pg.mixer.music.load('Music/Of Far Different Nature - 0 to 100 (CC-BY).ogg')
pg.mixer.music.set_volume(.5)  # 50% original volume
pg.mixer.music.play(-1, 0.0, 5000)
# endregion

# region load sfx
shoot_sound = lf.load_sound("556 Single Isolated.mp3", "sfx/556 Gunshots")
# endregion

# region Create The Background
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

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
sans_font = pg.font.Font('fonts/Pixeloid/TrueType (.ttf)/PixeloidSans.ttf', 32)

# @todo: just put the jpegs instead of descriptions.
title_text = sans_bold_font.render('SHOOT THE CIRCLE. DON\'T SHOOT THE X.', True, green, black)
title_text_rect = title_text.get_rect()
title_text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20)
# endregion

# region score setup
score = 0
score_increment = 10

score_text = sans_font.render(f'score: {score}', True, green, black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (
	SCREEN_WIDTH / 2, title_text_rect.bottom + score_text_rect.height)
# endregion
# endregion

player_reticle = gun.Gun("1.png", "sprites/green crosshairs")
good_targ = target.Target("168.png", "sprites/green crosshairs")
bad_targ = target.Target("152.png", "sprites/red crosshairs")

gun_sprite = pg.sprite.RenderPlain((player_reticle))
good_targ_sprite = pg.sprite.RenderPlain((good_targ))
bad_targ_sprite = pg.sprite.RenderPlain((bad_targ))
target_sprites = pg.sprite.RenderPlain((good_targ, bad_targ))

clock = pg.time.Clock()
pg.mouse.set_visible(False)

current_time = pg.time.get_ticks()
last_update = pg.time.get_ticks()
action_change_time = random.randint(1, 4) * 500  # 500 ms intervals
update_good_targ = random.randint(0, 2) == 0
update_bad_targ = random.randint(0, 2) == 1
update_none = random.randint(0, 2) == 2

# region game loop
while game_running:
	user_shot = False
	user_hit = False

	# event handler
	for event in pg.event.get():
		if event.type == pg.QUIT:
			game_running = False
		elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
			game_running = False
		elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			user_shot = True
			shoot_sound.play()
			if player_reticle.shoot(good_targ):
				user_hit = True
				good_targ.shot()
				score += score_increment
				score_text = sans_font.render(f'score: {score}', True, green, black)
			player_reticle.unshoot()  # reset player_reticle and immediately check for next target
			if player_reticle.shoot(bad_targ):
				user_hit = True
				bad_targ.shot()
				score -= score_increment
				if score < 0:
					score = 0
				score_text = sans_font.render(f'score: {score}', True, red, black)
		elif event.type == pg.MOUSEBUTTONUP:
			player_reticle.unshoot()

	# decrement score by half if shoot and no hits
	if user_shot and not user_hit:
		score -= score_increment / 2
		if score < 0:
			score = 0
		score_text = sans_font.render(f'score: {score}', True, yellow, black)
	
	gun_sprite.update()

	# draw everything
	screen.blit(background, (0, 0))
	screen.blit(title_text, title_text_rect)
	screen.blit(score_text, score_text_rect)

	if good_targ.hit:
		good_targ_sprite.update()
		good_targ_sprite.draw(screen)
	if bad_targ.hit:
		bad_targ_sprite.update()
		bad_targ_sprite.draw(screen)
	if update_good_targ:
		good_targ_sprite.draw(screen)
	elif update_bad_targ:
		bad_targ_sprite.draw(screen)
	
	gun_sprite.draw(screen)

	current_time = pg.time.get_ticks()
	if current_time - last_update >= action_change_time:
		target_sprites.update()
		last_update = current_time
		action_change_time = random.randint(1, 4) * 500 # 500 ms intervals
		update_good_targ = random.randint(0, 2) == 0
		update_bad_targ = random.randint(0, 2) == 1
		update_none = random.randint(0, 2) == 2

	pg.display.update()
# endregion

pg.quit()