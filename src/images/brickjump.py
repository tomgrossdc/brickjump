# brickjump.py
import sys
import pygame
from settings import Settings

bj_settings=Settings()

def run_game():
	pygame.init()
	screen=pygame.display.set_mode((bj_settings.screen_width,bj_settings.screen_height))
	pygame.display.set_caption("March UpHill")
