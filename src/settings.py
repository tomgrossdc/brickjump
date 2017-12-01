# settings.py brickjump
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

class Settings():
	def __init__(self):
		self.screen_width=1000
		self.screen_height=400
		self.bg_color=(230,230,230)
		self.bg_color=(255,222,173)
		self.brick_speed_factor = 1
		self.column_pos = self.screen_width
		self.brick_width = 10
		self.brick_height = 10
		self.brick_pile_number=0
		self.column_num = 0
		self.max_num_brick_climb = 1
		self.max_brick_steps = 1000
		self.column_heights= 1,2,3,2,1,2,1,2,2,4,1,2,3,4,8,6,5,4,3,4,5,6,1,2,4,4,5,8
		self.mousedownstill=False
		self.timecounter=0
		


	
