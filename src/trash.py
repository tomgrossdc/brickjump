# trash.py   just a place to hold bad old ideas

		self.clock = pygame.time.Clock()

		self.clock.tick(50)
        pygame.display.set_caption("fps: " + str(self.clock.get_fps()))


while True:
		screen.fill(bj_settings.bg_color)
		gf.check_events(bj_settings, screen, bricks,pickup)

		#brick.blitme()
		#bricknew.blitme()
#		gf.update_bricks(bj_settings,screen,bricks)
		bricks.update()
		runningman.update(bj_settings,bricks)
		bj_settings.column_pos -= bj_settings.brick_speed_factor
		if bj_settings.column_pos % bj_settings.brick_width == 0:
			bj_settings.column_num +=1
			if bj_settings.column_num >= len(bj_settings.column_heights):
				num_bricks=random.randint(1,8)
			else:
				num_bricks = bj_settings.column_heights[bj_settings.column_num]
			gf.create_column(bj_settings,screen,bricks,num_bricks)
		runningman.blitme()	
		bricks.draw(screen)
		pygame.display.flip()
		clock.tick(50)
		pygame.display.set_caption("fps: " + str(clock.get_fps()))
		time.sleep(.003)

		



		


pickedbricks=pygame.sprite.spritecollide(pickbrick,bricks, False)
	print ("yipes", len(pickedbricks))
	while len(pickedbricks)==1:
		pickbrick.rect.centery+=1
		print ("dropping",pickbrick.rect.centery,len(pickedbricks))
		pickedbricks=pygame.sprite.spritecollide(pickbrick,bricks, False)
	print ("dropped",pickbrick.rect.centery,len(pickedbricks))
	for test in pickedbricks :
		pickbrick.rect.centerx=test.rect.centerx
	return




















#
# Copyright (C) 2017 -  Tom Gross
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

#if (self.rect.x+self.rect.width >= col.rect.x+1 and
			#	self.rect.y+self.rect.height < col.rect.y+1 ): 
			#	FRT=True
			#if (self.rect.y+self.rect.height == col.rect.y+1 and 
			#	self.rect.x+self.rect.width < col.rect.x+1): 
			#	FLR=True
			#if FRT and not FLR : Front=True
			#if FLR : Floor = True
			i=i+1
			#print (i, self.rect.x+self.rect.width, col.rect.x, self.rect.y+self.rect.height, col.rect.y, Floor,Front)

			if dx<minx :	FLR = True
			if dy<miny:		FRT = True



						print (i, self.rect.centerx, col.rect.centerx, self.rect.centery, col.rect.centery, FLR,FRT)
		self.Floor = FLR
		self.Front = FRT
		#print (i, self.rect.centerx, self.rect.centery, self.Floor,self.Front)
		if self.state=="Climbing":
			if  self.climbing_time>=2*bj_settings.brick_height :
			#if Front and not Floor and self.climbing_time==2*bj_settings.brick_height :
				self.rect.x-=bj_settings.brick_speed_factor
				self.state="Falling"
				#self.climbing_time=0
			if self.Floor:
				self.state="Running"
				self.climbing_time=0	
				
		elif self.state == "Falling":
			self.climbing_time=0	
			if self.Floor and self.Front:
				self.state=="Climbing"
				self.rect.y-=self.man_up_speed
				self.climbing_time=0
			if self.Floor and not self.Front: 
				self.state="Running"
				
			# if falling hit new floor and still a wall the next IF will cause it to climb	
			
		elif self.state == "Running":
			if self.Front:
				self.state="Climbing"
			if not self.Floor:
				self.state="Falling"
				self.climbing_time=0


				This works but doesnt have 2 brick climb limiter
	def update(self,bj_settings,bricks):
		collisions = pygame.sprite.spritecollide(self,bricks,False)
		#Front=False
		#Floor=False
		i=0
		minx= 15
		miny=15
		d1y=1000
		d3x=1000
		dx=20000
		dy=20000
		FRT=False
		FLR=False
		lencol=len(collisions)
		for col in collisions :
			i+=1
			dx=min(dx,abs(self.rect.centerx-col.rect.centerx))
			dy=min(dy,abs(self.rect.centery-col.rect.centery))
			d1y=self.rect.y-col.rect.y
			if col.rect.y < self.rect.y :
				# col box is above runningman (ie colboxy is smaller than selfy) must be a wall
				#sign of d3x indicates: box in front - (climb) box behind + (run away)
				d3x=self.rect.x-col.rect.x
			print (i,"lencol=",lencol," self,col=",self.rect.x,self.rect.y,col.rect.x,col.rect.y,dx,dy,d1y,d3x)
		lencol=len(collisions)
		if lencol==0:
			#mid air, fall down till hit a floor
			if self.state=="Climbing":
				# climbed into the air. drop a bit and start running
				self.state="Running"
				self.rect.y+=self.man_up_speed
			else:
				self.state="Falling"
				print("else",self.state)
				
			print("0 overlap ",d1y,dx,dy,self.state)
		elif lencol==1:
			# straddling a top box corner or all floor or all front
			# if all floor or all front, dont change
			# if dy is equal to halfwidths then run forward (into air if needed)
			#if d1y==(bj_settings.brick_height-self.rect.height)/2:
			#	self.state="Running"

			# if falling goes to only one overlap, it must have hit a floor
			if self.state=="Falling":
				self.state="Running"
			print("1 overlap ",d1y,dx,dy)
		elif lencol==2:
			# either all floor or all front. Dont change
			if self.state=="Falling":
				self.state="Running"
			i=1
		elif lencol==3:	
			# corner. move up or forward, depending on min dx<0 for the brick which has highest y (min up)
			#sign of d3x indicates: box in front - (climb) box behind + (run away)
			if d3x<0 :
				self.state="Climbing"
			else:
				self.state="Running"
		else:
			# touching four at once? Already bad
			print("Four touchs",self.rect.x,self.rect.y,self.state," lencol=",lencol)
			sys.exit()
		
			

				
		print(self.rect.x,self.rect.y, self.state, self.climbing_time, lencol,self.rect.height,bj_settings.brick_height)


		if self.state=="Climbing":
			self.climbing_time +=1
			self.rect.y-=self.man_up_speed
			self.rect.x-=bj_settings.brick_speed_factor
		if self.state=="Running":
			# no wall in front, but a good floor, go forward
			self.rect.x+=self.man_forward_speed
		if self.state=="Falling":
			# no floor, fall
			self.rect.y+=self.man_up_speed
			self.rect.x-=bj_settings.brick_speed_factor
