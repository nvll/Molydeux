#!/usr/bin/python

from sprite import *
import pygame
from pygame.locals import *
from pygame.colordict import THECOLORS
global Sprites

texture_files = [
	"textures/environment.png",
	"textures/char.png"
]

texture_map = ({
	"=": (texture_files[0], 0, 2),
	"+": (texture_files[0], 1, 2),
	"x": (texture_files[0], 3, 2),
	"#": (texture_files[0], 4, 2),
	"^": (texture_files[0], 8, 6),
	" ": (texture_files[0], 7, 6),
})

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
			for x, val in enumerate(l.strip()):
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
				self[x, y].sprite = sprite_cache.get_sprite(texture_map[self[x, y].value])

	def draw_map(self, surface):
		for x in xrange(0, self.x):
			for y in xrange(0, self.y):
				surface.blit(self[x, y].sprite, (x * 32, y * 32)) 
def main():
	pygame.init()
	
	game_map = Map("map.txt")
	Sprites = SpriteCache()
	
	
	screen = pygame.display.set_mode((32 * game_map.x, 32 * game_map.y))
	Sprites.add_sheet(texture_files[0], 8, 8, (0, 255, 255))
	Sprites.add_sheet(texture_files[1], 8, 8, (0, 255, 255))
	game_map.load_sprites(Sprites)
	
	game_map.draw_map(screen)
	pygame.display.flip()

	while True:
		for e in pygame.event.get():
			if e.type == KEYDOWN:
				exit()

if __name__ == '__main__': main()
