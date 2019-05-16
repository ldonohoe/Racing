import pygame
from math import *
import Tracks

def init():
	x = 200
	y = 200
	width = 800
	height = 800

	pygame.init()
	degree = 0
	done = False
	screen = pygame.display.set_mode((width, height))
	innerPoints = Tracks.TRACKS[1]
	outerPoints = []
	while not done:
		screen.fill((0, 0, 0))
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True
			if event.type == pygame.MOUSEBUTTONDOWN:
				outerPoints += [event.pos]

		print(outerPoints)

		
		if len(outerPoints) > 1:
			print("Drawinggg")
			pygame.draw.lines(screen, (255, 255, 255), True, outerPoints)

		pygame.draw.lines(screen, (255, 255, 255), True, innerPoints)

		pygame.display.update()



def main():
	init()

if __name__ == "__main__":
	main()