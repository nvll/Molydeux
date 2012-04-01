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
	map_rows = 0
	map_cols = 0
	screen = None
	bg = None
	font = None

	def __init__(self):
		self.screen = pygame.display.set_mode((200, 250))
		pygame.display.set_caption("Friends?")
		self.bg = pygame.Surface(self.screen.get_size())
		self.font = pygame.font.SysFont("courier new", 20, 0, 0)
		self.load_map("map.txt")
	
	def validate_move(self, x, y):
		if x >= self.map_cols or x <= 0:
			return False

		if y >= self.map_rows or y <= 0:
			return False

		if self.mapdata[x][y] == '#':
			return False

		return True
		
	def move(self, key):
		new_x, new_y = self.pos_x, self.pos_y
		if key == K_UP:
			new_y = self.pos_y - 1
		elif key == K_DOWN:
			new_y = self.pos_y + 1
		elif key == K_LEFT:
			new_x = self.pos_x - 1
		elif key == K_RIGHT:
			new_x = self.pos_x + 1

		if self.validate_move(new_x, new_y):
			self.pos_x, self.pos_y = new_x, new_y

	def draw(self):
		# blabla bg color
		self.bg = self.bg.convert()
		self.bg.fill(THECOLORS['black'])
		text_top = 0

		# draw the map
		x_offset = 12
		y_offset = 24
		for y in xrange(0, self.map_rows):
			for x in xrange(0, self.map_cols):
				line = self.font.render(self.mapdata[x][y], 1, THECOLORS['grey'])
				self.bg.blit(line, (x * x_offset, y * y_offset))

		# draw the player
		player = self.font.render('@', 1, THECOLORS['green'])
		self.bg.blit(player, (self.pos_x * x_offset, self.pos_y * y_offset))

		self.screen.blit(self.bg, (0, 0))
		pygame.display.flip()
	
	def load_map(self, file):
		found_pos = False
		fd = open("map.txt")
		self.map_rows, self.map_cols = [int(x) for x in fd.readline().split()]
		print "map dimensions %dx%d" % (self.map_rows, self.map_cols)
		self.mapdata = [[[] for i in range(self.map_rows)] for j in range(self.map_cols)]
		for y, row in enumerate(fd.readlines()):
			for x, pos in enumerate(row.rstrip()):
				self.mapdata[x][y] = pos
				if not found_pos and pos == ' ':
					print "found pos at %d, %d" % (x, y)
					self.pos_x, self.pos_y = x, y
					found_pos = True

def main():
	
	state = GameState() 
	while True:
		state.draw()
		for e in pygame.event.get():
			if e.type == KEYDOWN:
				if e.key == K_q:
					key_input(e)
				else:
					state.move(e.key)

if __name__ == '__main__': main()


