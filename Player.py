import pygame
from math import *

class Player(object):
	def __init__(self, screen):
		self.x = 200
		self.y = 200
		self.velocity = 0
		self.direction = 1
		self.image = pygame.image.load('racecar.png')
		self.rect = self.image.get_rect()
		self.angle = 0
		self.velocity = 0
		self.screenWidth = screen.get_width()
		self.screenHeight = screen.get_height()
		self.location = self.rect


	def update_player(self):
		dX = cos(radians(self.angle)) * self.velocity
		dY = sin(radians(self.angle)) * self.velocity
		self.x += dX
		self.y += dY

		if self.x < 0:
			self.x = 0
			self.velocity = 0
		if self.y < 0:
			self.y = 0
			self.velocity = 0
		if self.x > self.screenWidth:
			self.x = self.screenWidth
			self.velocity = 0
		if self.y > self.screenHeight:
			self.y = self.screenHeight
			self.velocity = 0

		if self.angle >= 360:
			self.angle -= 360
		if self.angle < 0:
			self.angle += 360

		if self.velocity != 0:
			if self.velocity < 0:
				self.velocity +=1
			else:
				self.velocity -=1

	def handle_keys(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			# Rotate Left
			self.angle += -3 * self.direction

		if key[pygame.K_RIGHT]:
			#Rotate right
			self.angle += 3 * self.direction

		if key[pygame.K_UP]:
			if abs(self.velocity) < 15:
				self.velocity += 2
				self.direction = 1
		if key[pygame.K_DOWN]:
			if abs(self.velocity) < 15:
				self.velocity -= 2
				self.direction = -1
		


	def draw(self, screen):
		surf = pygame.Surface((50, 25))
		surf.fill((255, 255, 255))

		surf.set_colorkey((255, 0, 0))

		pygame.draw.rect(surf, (255, 255, 255), self.rect)
		xy = pygame.Rect(self.x, self.y, 50, 25)
		blitted = screen.blit(surf, xy)

		# Begin rotation
		oldCenter = blitted.center
		pygame.draw.rect(surf, (0, 0, 150), self.rect)
		rotatedSurf = pygame.transform.rotate(surf, -self.angle)

		rotRect = rotatedSurf.get_rect()
		rotRect.center = oldCenter

		#rotImage = pygame.transform.rotate(self.image, -self.angle)

		self.location = screen.blit(rotatedSurf, rotRect)
		#screen.blit(rotImage, rotRect)