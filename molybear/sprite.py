#!/usr/bin/python

import pygame
from pygame.locals import *
from pygame.colordict import THECOLORS

class SpriteCache:
	sprite_sheets = {}
	sprites = {}

	def add_sheet(self, filename, width, height, colorkey = None):
		self.sprite_sheets[filename] = SpriteLoader(filename, width, height, colorkey)

	def get_sprite(self, (filename, x, y)):
		id = (filename, x, y)
		if self.sprites.setdefault(id, None):
			return self.sprites[id]
		else:
			print "loaded sprite: ", id
			sprite = self.sprite_sheets[filename].get_sprite(x, y)
			sprite = pygame.transform.scale(sprite, (32, 32))
			self.sprites[id] = sprite
			return sprite

class SpriteLoader:
	sheet = None
	width = 0
	height = 0
	colorkey = ()
	sprite_cache = {}

	def __init__(self, path, width, height, colorkey = None):
		self.sheet = pygame.image.load(path)

		if colorkey is not None:
			self.sheet.set_colorkey(colorkey, RLEACCEL)
			self.colorkey = colorkey
		
		self.width = width
		self.height = height

	def get_sprite(self, x, y):
		if x * self.width > self.sheet.get_width() or y * self.height > self.sheet.get_height():
			return None

		rect = pygame.Rect((x * self.width, y * self.height, self.width, self.height))
		sprite = pygame.Surface(rect.size).convert()
		sprite.blit(self.sheet, (0, 0), rect)
		sprite = sprite.convert()
		if self.colorkey:
			sprite.set_colorkey(self.colorkey, RLEACCEL)

		return sprite 
	
def main():
	s_x = s_y = 0

	screen = pygame.display.set_mode((32, 32))
	screen.fill(THECOLORS['white'])
	env_sprites = SpriteCache()
	env_sprites.add_sheet("textures/environment.png", 8, 8, (0, 255, 255))
	
	while True:
		for e in pygame.event.get():
			if e.type == KEYUP:
				if e.key == K_RIGHT:
					s_x += 1
				elif e.key == K_LEFT:
					s_x -= 1
				elif e.key == K_UP:
					s_y -= 1
				elif e.key == K_DOWN:
					s_y += 1
				elif e.key == K_q:
					exit()

		if s_x < 0:
			s_x = 0
		if s_y < 0:
			s_y = 0

		sprite = env_sprites.get_sprite("textures/environment.png", s_x, s_y)
		sprite = pygame.transform.scale(sprite, (32, 32))
		screen.blit(sprite, (0, 0))
		pygame.display.flip()

if __name__ == '__main__': main()
