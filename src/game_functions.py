# game_functionimport sys
import sys
import pygame
from pygame.sprite import Sprite
from time import sleep
import random

from brick import Brick

def check_events(bj_settings, screen, bricks, pickup):
	""" Respond to keypresses and mouse events """
	KeyReturn=False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			KeyReturn=check_keydown_events(event,bj_settings, screen, bricks)
		elif event.type == pygame.MOUSEBUTTONDOWN:	
			# pickedbrick is return True of False.  The sprite is bj_setting.pickbrick).
			pickedbrick = pickupbrick(bj_settings,screen,bricks,pickup)
			if pickedbrick : bj_settings.mousedownstill=True
		elif event.type == pygame.MOUSEMOTION:
			if bj_settings.mousedownstill: movepickedbrick(bj_settings.pickbrick)
		elif event.type == pygame.MOUSEBUTTONUP:
			droppickedbrick(bj_settings, bj_settings.pickbrick,bricks)
			bj_settings.mousedownstill=False
	return KeyReturn

def droppickedbrick(bj_settings, pickbrick,bricks):
# Keep dropping (outside main time loop) and testing for intercepts. 
# If brick is touching a brick within 1/2 width, set it down
	#print ( "Droppickedbrick",pickbrick.rect.centery)
	if not pickbrick : return
	dropping=True
	while dropping:
		pickbrick.rect.centery+=1
		if pickbrick.rect.centery>bj_settings.screen_height : dropping=False
		pickedbricks=pygame.sprite.spritecollide(pickbrick,bricks, False)
		#print ( "droppickedbrick",pickbrick.rect.centery, len(pickedbricks),pickbrick.rect.centerx,pickbrick.rect.width/2)
		for test in pickedbricks :

			if test.brickserielnumber<>pickbrick.brickserielnumber:
				#print ( "droppickedbrick",pickbrick.rect.centery, len(pickedbricks),abs(test.rect.centerx-pickbrick.rect.centerx),pickbrick.rect.width/2)

				# Test for a brick centered
				if abs(test.rect.centerx-pickbrick.rect.centerx)<pickbrick.rect.width/2 :
					# Test for a brick above and centered
					if pickbrick.rect.y > test.rect.y:
						# move up steps instead to top of heap
						pickbrick.rect.y-=1
						
					else:
						# move back a step, center and stop dropping
						pickbrick.rect.y-=1
						pickbrick.rect.centerx=test.rect.centerx
						dropping=False
	pickbrick.pickedbrick=False
	
	
def movepickedbrick(pickbrick):
	mousepos=pygame.mouse.get_pos()
	pickbrick.rect.centerx = mousepos[0]
	pickbrick.rect.centery = mousepos[1]
	return
			
def pickupbrick(bj_settings,screen,bricks,pickup):
	mousepos=pygame.mouse.get_pos()
	pickup.rect.x = mousepos[0]
	pickup.rect.y = mousepos[1]
	pickedbricks=pygame.sprite.spritecollide(pickup,bricks, False)
	print ("Mouse at:",mousepos,pickup.rect,len(pickedbricks))	
	if len(pickedbricks)==0 : 
		# No Selection
		#pickbrick=False
		return False
	else:
		#check for top brick
		for pickbrick in pickedbricks:
			pickbrick.rect.centerx=pickbrick.rect.centerx
		
		BrickBelow = False
		BrickAbove = False
		for test in bricks:
			if (test.brickserielnumber==pickbrick.brickserielnumber+1) and test.rect.centerx==pickbrick.rect.centerx : BrickAbove=True
			if (test.brickserielnumber==pickbrick.brickserielnumber-1) and test.rect.centerx==pickbrick.rect.centerx : BrickBelow=True


		if not BrickAbove and BrickBelow and not pickbrick.pickedbrick:
		#if BrickAbove==False and BrickBelow==True:
			pickbrick.rect.centerx=pickup.rect.x
			pickbrick.rect.centery=pickup.rect.y
			bj_settings.pickbrick=pickbrick
			pickbrick.pickedbrick=True
			return True
		else:
			return False

	return False	


	
def check_keydown_events(event, bj_settings, screen, brick):
	KeyDown=False
	if  event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_s:
		sys.exit()
	elif event.key == pygame.K_r:
		KeyDown=True
	return KeyDown
		

def update_bricks(bj_settings,screen,bricks):
	bricks.update()

def create_brick(bj_settings,screen,bricks,brick_number,Last):
	bricknew=Brick(bj_settings,screen)
	bricknew.rect.y -= brick_number*bricknew.rect.height
	if Last: 
		bricknew.image=pygame.image.load('images/redbrick753.bmp')
		bricknew.pickedbrick=False
	bricks.add(bricknew)

def update_columns(bj_settings,screen,bricks,num_bricks):		
	bj_settings.column_pos -= bj_settings.brick_speed_factor
	if bj_settings.column_pos % bj_settings.brick_width == 0:
		bj_settings.column_num +=1
		if bj_settings.column_num >= len(bj_settings.column_heights):
			num_bricks=random.randint(1,8)
		else:
			num_bricks = bj_settings.column_heights[bj_settings.column_num]
		create_column(bj_settings,screen,bricks,num_bricks)
			

def create_column(bj_settings,screen,bricks,num_bricks):
	for brick_number in range(num_bricks):
		Last=False
		if brick_number==num_bricks-1: Last=True
		create_brick(bj_settings,screen,bricks,brick_number,Last)
		
