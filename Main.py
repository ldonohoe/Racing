import pygame, Map
from math import *
from Player import Player
from Camera import Camera
from Traffic import *
from Police import Police

def init(screen):
	pygame.init()

	title = pygame.image.load('resources/Title.png')

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


		screen.blit(title, pygame.Rect(0, 0, 1000, 1000))





def game(screen):

	background = pygame.Surface(screen.get_size())
	background = background.convert_alpha()
	background.fill((26, 26, 26))
	font = pygame.font.Font(None, 24)


	done = False
	clock = pygame.time.Clock()
	player = Player()
	camera = Camera()


	player_s 	= pygame.sprite.Group() # Handles player movements and updates
	map_s 		= pygame.sprite.Group() # Handles map movements
	traffic_s 	= pygame.sprite.Group()
	police_s 	= pygame.sprite.Group()

	for i in range(0, 5):
		traffic_s.add(Traffic())
		police_s.add(Police())


	# Load map files
	for tile in range(0, len(Map.map_tiles)):
		Map.map_files.append(pygame.image.load('resources/' + Map.map_tiles[tile]))
	# Create map
	for x in range(0, 10):
		for y in range(0, 10):
			map_s.add(Map.Map(Map.map_1[x][y], x * 1000, y * 1000, Map.map_1_rot[x][y]))


	player_s.add(player)
	camera.setCam(player.x, player.y)

	w_center = int(pygame.display.Info().current_w/2)
	h_center = int(pygame.display.Info().current_h/2)

	initTraf(w_center, h_center)

	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True	

		screen.blit(background, (0,0))


		map_s.update(camera.x, camera.y)
		map_s.draw(screen)

		# Check driving surface
		carGround = screen.get_at((w_center, h_center))
		player.handle_keys()	
		player.update_player(carGround)
		camera.setCam(player.x, player.y)

		player_s.update(camera.x, camera.y)
		player_s.draw(screen)

		traffic_s.update(camera.x, camera.y)
		traffic_s.draw(screen)

		police_s.update(camera.x, camera.y)
		police_s.draw(screen)


		text_fps = font.render('FPS: ' + str(int(clock.get_fps())), 1, (224, 16, 16))
		textpos_fps = text_fps.get_rect(centery=25, centerx=60)
		screen.blit(text_fps, textpos_fps)
		
		text_boost = font.render('BOOST: ', 1, (0, 0, 250))
		textpos_boost = text_boost.get_rect(centery=pygame.display.Info().current_h-65, centerx=pygame.display.Info().current_w-235)
		screen.blit(text_boost, textpos_boost)
		pygame.draw.rect(screen, (0, 0, 250), player.boostBar())

		text_speed = font.render("SPEED: " + str(player.velocity), 1, (224, 16, 16))
		textpos_speed = text_speed.get_rect(centery=40, centerx=60)
		screen.blit(text_speed, textpos_speed)



		pygame.display.flip()

		clock.tick(50)


def main():
	pygame.init()
	screen = pygame.display.set_mode((pygame.display.Info().current_w,
                                  pygame.display.Info().current_h))
	init(screen)

if __name__ == '__main__':
	main()

