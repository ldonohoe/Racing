import pygame
from Tracks import TRACKS
from math import *
from Player import Player

def init(screen):
	pygame.init()
	speed = [2, 2]
	RED = (255, 0, 0)
	WHITE = (255, 255, 255)

	screen.fill(WHITE)
	player = Player(screen)

	done = False
	clock = pygame.time.Clock()
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print("Clicked")
			elif event.type == pygame.MOUSEBUTTONUP:
				print("Unclicked")

		screen.fill((255, 255, 255))


		#track = pygame.Rect(200, 200, 3, 200)

		#pygame.draw.rect(screen, (0, 0, 0), track)

		player.draw(screen)
		player.handle_keys()	
		player.update_player()
		pygame.display.update()

		clock.tick(40)


def main():
	size = width, height = 800, 800
	pygame.init()
	screen = pygame.display.set_mode(size)
	init(screen)

if __name__ == '__main__':
	main()

