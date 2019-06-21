import pygame, Map
from math import *
from Player import Player
from Camera import Camera

def init(screen):
	pygame.init()
	RED = (255, 0, 0)
	WHITE = (255, 255, 255)

	screen.fill(WHITE)

	start = pygame.Rect(200, 200, 300, 200)
	pygame.draw.rect(screen, (255, 0, 0), start)

	done = False
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print("Clicked")
			elif event.type == pygame.MOUSEBUTTONUP:
				print("Unclicked")
				game(screen)

		pygame.draw.rect(screen, (255, 0, 0), start)




def game(screen):

	background = pygame.Surface(screen.get_size())
	background = background.convert_alpha()
	background.fill((26, 26, 26))

	done = False
	clock = pygame.time.Clock()
	player = Player()
	camera = Camera()


	player_s 	= pygame.sprite.Group()
	map_s 		= pygame.sprite.Group()


	# Generate map
	for tile in range(0, len(Map.map_tiles)):
		Map.map_files.append(pygame.image.load('resources/' + Map.map_tiles[tile]))
	for x in range(0, 10):
		for y in range(0, 10):
			map_s.add(Map.Map(Map.map_1[x][y], x * 1000, y * 1000, Map.map_1_rot[x][y]))


	player_s.add(player)
	camera.setCam(player.x, player.y)


	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True	

		screen.blit(background, (0,0))


		player.handle_keys()	
		player.update_player()
		camera.setCam(player.x, player.y)

		map_s.update(camera.x, camera.y)
		map_s.draw(screen)

		player_s.update(camera.x, camera.y)
		player_s.draw(screen)



		pygame.display.flip()

		clock.tick(64)


def main():
	size = width, height = 800, 800
	pygame.init()
	screen = pygame.display.set_mode(size)
	init(screen)

if __name__ == '__main__':
	main()

