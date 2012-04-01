#!/usr/bin/python

from sprite import *
import pygame
from pygame.locals import *
from pygame.colordict import THECOLORS
from texture import *

# Contains all information about a map tile in the game world
class MapTile():
	value = 0
	sprite = None
	entity = None
	valid_move = False
	def __init__(self, value, entity = None):
		self.value = value
		self.sprite = None
		self.entity = entity
		self.valid_move = False
	
class Map():
	map_data = []
	x = 0
	y = 0
	def __init__(self, filename):
		# peek at map header and initialize
		fd = open(filename)
		self.x, self.y = [int(x) for x in fd.readline().split()]
		self.map_data = [0] * self.x * self.y 
		
		for y, l in enumerate(fd.readlines()):
			if y >= self.y:
				break
			for x, val in enumerate(l[:-1]):
				if x >= self.x:
					break
				self[x, y] = MapTile(val)

	def __getitem__(self, (x, y)):
		if x >= self.x or y >= self.y:
			return None
		else:
			return self.map_data[(y * self.x) + x]

	def __setitem__(self, (x, y), value):
		if x >= self.x or y >= self.y:
			raise IndexError("Map: [%d, %d] is out of bounds [%d, %d]" % (x, y, self.x, self.y))
		else:
			self.map_data[(y * self.x) + x] = value
	
	def load_sprites(self, sprite_cache):
		for x in xrange(0, self.x):
			for y in xrange(0, self.y):
				sprite_id, movable = object_map[self[x, y].value]
				self[x, y].sprite = sprite_cache.get_sprite(sprite_id)
				self[x, y].valid_move = movable

	def draw_map(self, surface):
		for x in xrange(0, self.x):
			for y in xrange(0, self.y):
				surface.blit(self[x, y].sprite, (x * 32, y * 32)) 

				if self[x, y].entity:
					surface.blit(self[x, y].entity.get_sprite(), (x * 32, y * 32), None, 0)
def main():
	pygame.init()
	
	game_map = Map("map.txt")
	Sprites = SpriteCache()
	
	
	screen = pygame.display.set_mode((32 * game_map.x, 32 * game_map.y))
	Sprites.add_sheet(texture_files[0], 8, 8, (0, 255, 255))
	Sprites.add_sheet(texture_files[1], 8, 8, (0, 255, 255))
	game_map.load_sprites(Sprites)
	

	while True:
		for e in pygame.event.get():
			if e.type == KEYDOWN:
				exit()
		game_map.draw_map(screen)
		pygame.display.flip()

if __name__ == '__main__': main()
