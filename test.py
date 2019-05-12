import pygame
from math import *





def init():
	x = 200
	y = 200
	width = 800
	height = 800
	velocity = 0
	maxVeloc = 15
	direction = 1
	image = pygame.image.load('racecar.png')

	pygame.init()
	degree = 0
	done = False
	screen = pygame.display.set_mode((width, height))
	while not done:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True

		if velocity != 0:
			if velocity < 0:
				velocity +=1
			else:
				velocity -=1
		screen.fill((255, 255, 255))
		surf = pygame.Surface((50, 25))
		surf.fill((255, 255, 255))

		surf.set_colorkey((255, 0, 0))
		big = pygame.Rect(0, 0, 25, 25)
		small = pygame.Rect(0, 25, 25, 25)

		pygame.draw.rect(surf, (255, 255, 255), big)
		pygame.draw.rect(surf, (255, 50, 255), small)
		xy = pygame.Rect(x, y, 50, 25)
		blitted = screen.blit(surf, xy)

		# Begin rotation
		oldCenter = blitted.center
		rotatedSurf = pygame.transform.rotate(surf, -degree)

		rotRect = rotatedSurf.get_rect()
		rotRect.center = oldCenter

		rotImage = pygame.transform.rotate(image, -degree)

		screen.blit(rotatedSurf, rotRect)
		screen.blit(rotImage, rotRect)


		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			# Rotate Left
			#if (self.angle < self.maxAngle):
			degree += -3 * direction
			print("Left")

		if key[pygame.K_RIGHT]:
			#Rotate right
			#if (abs(self.angle) < self.maxAngle):
			degree += 3 * direction
			print("Right")

		if key[pygame.K_UP]:
			if abs(velocity) < maxVeloc:
				velocity += 2
				direction = 1
		if key[pygame.K_DOWN]:
			if abs(velocity) < maxVeloc:
				velocity -= 2
				direction = -1

			
		dX = cos(radians(degree)) * velocity
		dY = sin(radians(degree)) * velocity
		x += dX
		y += dY

		if x < 0:
			x = 0
		if y < 0:
			y = 0
		if x > width:
			x = width
		if y > height:
			y = height

		if degree >= 360:
			degree -= 360
		if degree < 0:
			degree += 360

		pygame.display.flip()
		#pygame.display.update()
		pygame.time.wait(10)


def main():
	init()

if __name__ == "__main__":
	main()