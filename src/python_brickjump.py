#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py   python_brickjump.py
# Copyright (C) 2017  Tom Gross <tgrossdc@gmail.com>
# 
# python-brickjump is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# python-brickjump is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import time

import pygame
from pygame.sprite import Group
from pygame.sprite import LayeredUpdates 
from pygame.time import Clock
from settings import Settings
from brick import Brick
from brick import Pickup
import game_functions as gf
from runningman import RunningMan

bj_settings=Settings()

def reset_game(bj_settings,screen,num_bricks):
	
	# Set up the Group of bricks LayeredUpdates is a class that uses Group, 
	# so it has added features, like  Nothing 
	bricks = Group()
	#bricks.add(brick)
	#bricknew = Brick(bj_settings,screen)
	#bricknew.rect.y -= bricknew.rect.height
	#bricks.add(bricknew)
	#num_bricks=6
	#gf.create_column(bj_settings,screen,bricks,num_bricks)
	
	""" Make most recent screen visible"""
	""" Start up the bricks with a floor, then add running man"""
	bj_settings.column_pos = bj_settings.screen_width
	while bj_settings.column_pos>0:
		screen.fill(bj_settings.bg_color)
		#gf.check_events(bj_settings, screen, brick, pickup)
		bricks.update()
		bj_settings.column_pos -= bj_settings.brick_speed_factor
		#print ("columnpos=",bj_settings.column_pos)

		if bj_settings.column_pos % bj_settings.brick_width == 0 :
			gf.create_column(bj_settings,screen,bricks,num_bricks)	
		#bricks.draw(screen)
		#pygame.display.flip()
		#time.sleep(.003)
	return bricks

def run_game():
	pygame.init()
	screen=pygame.display.set_mode((bj_settings.screen_width,bj_settings.screen_height))
	pygame.display.set_caption("GitHub Version DecBranch brickjump.py")
	clock = pygame.time.Clock()
	#Lay a brick
	brick = Brick(bj_settings,screen)
	pickup = Pickup(bj_settings,screen)
	print("pickup sprite",pickup.rect.x)
	num_bricks=1
	bricks=reset_game(bj_settings,screen,num_bricks)
	
	#
	# Add a running man standing on top of first brick, with 2x forward speed
	runningman=RunningMan(bj_settings,screen)
	#collisions = pygame.sprite.spritecollide(runningman,bricks,False)
	#for col in collisions :
	#	runningman.rect.centerx = col.rect.centerx
	#	runningman.rect.centery = col.rect.centery -(col.rect.height+runningman.rect.height)/2
		
	while True:
		screen.fill(bj_settings.bg_color)
		ReStartOnR=gf.check_events(bj_settings, screen, bricks,pickup)
		if runningman.rect.centerx<0: ReStartOnR=True
		if runningman.rect.centerx>bj_settings.screen_width: ReStartOnR=True
		if ReStartOnR:
			bricks=reset_game(bj_settings,screen,num_bricks)
			runningman.rect.centerx = 2*bj_settings.brick_width
			runningman.rect.centery = bj_settings.screen_height-3*runningman.rect.height
		
		#brick.blitme()
		#bricknew.blitme()
#		gf.update_bricks(bj_settings,screen,bricks)
		bricks.update()
		runningman.update(bj_settings,bricks)
		gf.update_columns(bj_settings,screen,bricks,num_bricks)
		
		runningman.blitme()	
		bricks.draw(screen)
		pygame.display.flip()
		clock.tick(50)
		pygame.display.set_caption("GitHub Version DecBranch brickjump.py fps: " + str(clock.get_fps()))
		time.sleep(.003)


print "brickjump.py from Anjuta Programmes/python-brickjump/src"
print "r-> reset ; s-> stop"
run_game()

