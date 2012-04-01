#!/usr/bin/python
from texture import *
class Entity:
	map_ref = None
	x = 0
	y = 0
	move_wait = 0
	alive = True
	sprite = None
	sprite_alive = None
	sprite_dead = None
	player = False
	oxygen = 100
	
	def __init__(self, x, y, map_ref, alive_id, dead_id, sprite_cache, player = False):
		self.map_ref = map_ref
		self.x, self.y = x, y
		self.player = player
		
		self.sprite_alive = sprite_cache.get_sprite(object_map[alive_id][0])
		self.sprite_dead = sprite_cache.get_sprite(object_map[dead_id][0])

		if not self.move_to(x, y):
			print "couldn't place entity"
	
	def move_left(self):
		self.move_to(self.x - 1, self.y)
	
	def move_right(self):
		self.move_to(self.x + 1, self.y)

	def move_up(self):
		self.move_to(self.x, self.y - 1)

	def move_down(self):
		self.move_to(self.x, self.y + 1)

	def move_to(self, x, y):
		if self.valid_move(x, y):
			entity = self.map_ref[x, y].entity
			if entity and self.player:
				if entity.alive:
					entity.alive = False
					self.oxygen += 40

			self.map_ref[self.x, self.y].entity = None
			self.x, self.y = x, y
			self.map_ref[self.x, self.y].entity = self
			return True

		return False

	def valid_move(self, x, y):
		if not self.alive:
			return False
		if x < 0 or x >= self.map_ref.x:
			return False
		if y < 0 or y >= self.map_ref.y:
			return False
		if not self.map_ref[x, y].valid_move:
			return False

		return True

	def get_sprite(self):
		if self.alive:
			return self.sprite_alive
		else:
			return self.sprite_dead
	
		
