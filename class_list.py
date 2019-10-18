"""list of class for MacGyver Escape game"""

import pygame
from pygame.locals import *
from constants import *
import random

class Level:
	"""Creating the level"""
	def __init__(self, file):
		self.file = file
		self.structure = 0

	def generate(self):
		"""this method allow to generate a level_structure from the Labyrinth File"""

		with open(self.file, "r") as file:

			level_structure = []

			#We go through the Labyrinth file filling the main list "level_structure" with sublist "level_line"

			for line in file:
				level_line = []
				for sprite in line:
					if sprite != '\n':
						level_line.append(sprite)

				level_structure.append(level_line)

			#we save this strucutre in the attribute level.structure
			self.structure = level_structure

	def display(self, window):
		"""Method for displaying the level according to the structure list returned by generate ()"""
		wall = pygame.image.load(picture_wall).convert()
		start = pygame.image.load(picture_start).convert()
		end = pygame.image.load(picture_end).convert_alpha()


		num_line = 0
		for line in self.structure:
			#We go through the lists of lines, displaying the corresponding picture depending on the sprite value
			num_sprite = 0
			for sprite in line:
				x = num_sprite * sprite_size
				y = num_line * sprite_size
				if sprite == '#':
					window.blit(wall, (x,y))
				elif sprite == 'd':
					window.blit(start, (x,y))
				elif sprite == 'a':
					window.blit(end, (x,y))
				num_sprite += 1
			num_line += 1



class Char :
	""" Class to create a character"""
	def __init__(self, skin, level):

		self.skin = pygame.image.load(skin).convert_alpha()
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.level = level


	def move(self, direction):
		"""Method for moving the character"""

		#For each direction we need to check 2 things before to move Mac : no wall and no "map" border
		if direction == 'right':

			if self.case_x < (sprite_by_side - 1) and self.level.structure[self.case_y][self.case_x+1] != '#':
					self.case_x += 1
					self.x = self.case_x * sprite_size

		elif direction == 'left':
			if self.case_x > 0 and self.level.structure[self.case_y][self.case_x-1] != '#':
					self.case_x -= 1
					self.x = self.case_x * sprite_size

		elif direction == 'up':
			if self.case_y > 0 and self.level.structure[self.case_y-1][self.case_x] != '#':
					self.case_y -= 1
					self.y = self.case_y * sprite_size

		elif direction == 'down':
			if self.case_y < (sprite_by_side - 1) and self.level.structure[self.case_y+1][self.case_x] != '#':
					self.case_y += 1
					self.y = self.case_y * sprite_size

class Item:
	""" Class to create an object"""
	def __init__(self, skin, level):

		self.skin = pygame.image.load(skin).convert_alpha()
		self.picked = 0
		self.level = level
		self.case_y = random.randint(0, 14)
		self.case_x = random.randint(0, 14)
		#Get a random position for the object, if not on a free spot, randomize again
		while self.level.structure[self.case_y][self.case_x] != " ":
			self.case_y = random.randint(0, 14)
			self.case_x = random.randint(0, 14)


	def generate(self, window, MacGyver):
		"""Method for generate the object and handle the picking"""
		#If Macgyver get on the object position
		if self.case_x == MacGyver.case_x and self.case_y == MacGyver.case_y:

			self.picked = 1
		#If Object not picked : display it
		if self.picked == 0 :
			x = self.case_x * sprite_size
			y = self.case_y * sprite_size

			window.blit(self.skin,(x,y))
