
"""
MacGyver Escape Again Game :

MacGyver has to get every items and find a way to leave

File: Macescape.py, class_list.py, constants.py, Labyrinth, picture folder

"""

import pygame
from pygame.locals import *

from class_list import *
from constants import *

pygame.init()

#Pygame's window initialization
window = pygame.display.set_mode((window_size, window_size))
icon = pygame.image.load(picture_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption(window_title)

home = pygame.image.load(picture_home).convert()
win = pygame.image.load(you_win).convert()
lose = pygame.image.load(you_lose).convert()
background = pygame.image.load(picture_background).convert()



#MAIN LOOP
main_loop = 1
game_loop = 0

while main_loop:

	home_loop = 1

	#HOME LOOP
	while home_loop:

		pygame.time.Clock().tick(30)

		# while in home_loop, we display one of the 3 home page, we can quit the loop with ESCAPE/QUIT
		# or get into the game (again) with space

		if game_loop == 2:
			window.blit(win, (0,0))
		elif game_loop == 3:
			window.blit(lose, (0,0))
		else :
			window.blit(home, (0,0))

		pygame.display.flip()



		for event in pygame.event.get():

			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				home_loop = 0
				game_loop = 0
				main_loop = 0



			elif event.type == KEYDOWN:
				#game launch
				if event.key == K_SPACE:
					home_loop = 0 	#Leaving home loop


					#Creating the level from the file "Labyrinth"
					level = Level("Labyrinth")
					level.generate()
					MacGyver = Char("images/MacGyver.png", level)
					ether = Item("images/ether.png", level)
					syringe = Item("images/syringe.png", level)
					needle = Item ("images/needle.png", level)

					game_loop = 1
	#GAME LOOP
	while game_loop == 1:

		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#During the game we look for "moves" input and we display the new position of
			#Macgyver at each loop

			if event.type == QUIT:
				game_loop = 0
				main_loop = 0

			elif event.type == KEYDOWN:
				#If the user press Esc here, we return only to the menu
				if event.key == K_ESCAPE:
					game_loop = 0

				#MacGyver moving keys
				elif event.key == K_RIGHT:
					MacGyver.move('right')
				elif event.key == K_LEFT:
					MacGyver.move('left')
				elif event.key == K_UP:
					MacGyver.move('up')
				elif event.key == K_DOWN:
					MacGyver.move('down')

		#For each game loop we refresh and display the new position of MacGyver
		window.blit(background, (0,0))
		level.display(window)
		ether.generate(window, MacGyver)
		syringe.generate(window, MacGyver)
		needle.generate(window, MacGyver)
		window.blit(MacGyver.skin , (MacGyver.x, MacGyver.y))
		pygame.display.flip()

		#If all items picked  -> back to home (WIN home) else -> back to home (LOSE home)
		if level.structure[MacGyver.case_y][MacGyver.case_x] == 'a' and ether.picked == 1 and syringe.picked == 1 and needle.picked == 1:
			game_loop = 2
		if level.structure[MacGyver.case_y][MacGyver.case_x] == 'a' and (ether.picked == 0 or syringe.picked == 0 or needle.picked == 0):
			game_loop = 3
