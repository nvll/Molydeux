#!/usr/bin/python

import pygame
from pygame.locals import *

def read_sprite(ssheet, x, y):
	rect = pygame.Rect((x * 8, y * 8, 8, 8))
	image = pygame.Surface(rect.size).convert()
	image.blit(ssheet, (0, 0), rect)
	
	return image

def main():
	screen = pygame.display.set_mode((32, 32))
	ssheet = pygame.image.load("textures/environment.png").convert_alpha(screen)
	ssheet.set_colorkey((0, 255, 255), 0)
	
	s_x, s_y = 0, 0
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

		if s_x < 0:
			s_x = 0
		if s_y < 0:
			s_y = 0

		sprite = read_sprite(ssheet, s_x, s_y)
		scaled = pygame.transform.scale(sprite, (screen.get_width(), screen.get_height()))
		screen.blit(scaled, (0, 0))
		pygame.display.flip()

if __name__ == '__main__': main()
