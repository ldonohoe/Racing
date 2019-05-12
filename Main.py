import pygame
from math import *

class Player(object):
    def __init__(self):
        self.image = pygame.image.load('racecar.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.angle = 0
        self.velocity = 0
        self.surf = pygame.Surface((self.width, self.height))
       	self.surf.fill((0, 0, 50))
        self.maxAngle = self.angle + 15

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 20
        if key[pygame.K_LEFT]:
            # Rotate Left
            #if (self.angle < self.maxAngle):
            self.angle += 2
            print("Left")

        if key[pygame.K_RIGHT]:
            #Rotate right
            #if (abs(self.angle) < self.maxAngle):
            self.angle += -2
            print("Right")

        if key[pygame.K_UP]:
            # Move Forward
            dX = cos(radians(self.angle)) * dist
            dY = sin(radians(self.angle)) * dist
            print("{}, {}".format(dX, dY))
            self.rect.move_ip(dX, dY)
            print("Up")

        if key[pygame.K_DOWN]:
            # Move Backward
            dX = floor(cos(radians(self.angle)) * -dist)
            dY = floor(sin(radians(self.angle)) * -dist)
            print("{}, {}".format(dX, dY))
            self.rect.move_ip(dX, dY)
            print("Down")


    def draw(self, screen):
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((0, 0, 0))
        self.surf.set_colorkey((255, 0, 0))

        oldCenter = screen.blit(self.surf, self.rect).center
        rotSurf = pygame.transform.rotate(self.surf, self.angle)
        rotRect = rotSurf.get_rect()
        rotRect.center = oldCenter
        rotImage = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotSurf, rotRect)
        screen.blit(rotImage, rotRect)




    def printCoords(self):
    	print("{}, {}, {}, {}".format(self.rect.bottomleft, self.rect.bottomright, self.rect.topleft, self.rect.topright))
    	print("{}".format(self.angle))
    
    def rotate_point(self, x, y, angle, p):
        s = math.sin(angle)
        c = math.cos(angle)

        pX = p[0]
        pY = p[1]
        pX -= x
        pY -= y

        newX = pX * c - pY * s
        newY = pX * s + pY * c

        pX += newX
        pY += newY

        return (pX, pY)



def init(screen):
	pygame.init()
	speed = [2, 2]
	RED = (255, 0, 0)
	WHITE = (255, 255, 255)

	screen.fill(WHITE)
	player = Player()

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

		player.draw(screen)
		player.handle_keys()
		pygame.display.update()

		clock.tick(40)


def main():
	size = width, height = 600, 400
	screen = pygame.display.set_mode(size)
	init(screen)

if __name__ == '__main__':
	main()

