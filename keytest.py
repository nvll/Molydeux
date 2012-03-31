#!/usr/bin/python

from sys import *
import pygame
from pygame.locals import *
from pygame.colordict import THECOLORS

pygame.display.init()
pygame.font.init()

class GameState:	
	pos_x = 0
	pos_y = 0
	mapdata = []
	screen = None
	bg = None
	font = None

	def __init__(self):
		self.screen = pygame.display.set_mode((400, 400))
		pygame.display.set_caption("Friends?")
		self.bg = pygame.Surface(self.screen.get_size())
		self.font = pygame.font.SysFont("courier new", 20, 0, 0)
		self.load_map("map.txt")
	
	def draw(self):
		self.bg = self.bg.convert()
		self.bg.fill(THECOLORS['black'])
		text_top = 0
		for l in self.mapdata:
			line = self.font.render(l.rstrip(), 1, THECOLORS['white'])
			text_pos = line.get_rect()
			self.bg.blit(line, (text_pos.left, text_top))
			text_top += (text_pos.bottom - text_pos.top)
			print "text top npw %d" % (text_top)
		self.screen.blit(self.bg, (0, 0))
		pygame.display.flip()
	
	def load_map(self, file):
		self.mapdata = open(file).readlines()
		for x, line in enumerate(self.mapdata):
			for y, pos in enumerate(line):
				if pos == ' ':
					print "Found starting spot at (%d, %d)" % (x, y)
					pos_x, pos_y = x, y
					return

def main():
	
	state = GameState() 
	state.draw()
	while True:
		for e in pygame.event.get():
			if e.type == KEYDOWN:
			#	print "top %d bottom %d" % (textpos.top, textpos.bottom)
				key_input(e)

def load_assets(state):
	return

def key_input(event):
	if event.key == K_q:
		pygame.quit()
	
if __name__ == '__main__': main()


