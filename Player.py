import pygame
from math import *
from pygame.locals import *

GRASS = 200


def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = int(pygame.display.Info().current_w /2)
		self.y = int(pygame.display.Info().current_h /2)
		self.velocity = 0
		self.direction = 1
		self.image = pygame.image.load('resources/blue_car.png')
		colorkey = self.image.get_at((0,0))
		self.image.set_colorkey(colorkey, RLEACCEL)
		self.image_orig = self.image
		self.rect = self.image.get_rect()
		self.rect.topleft = self.x, self.y
		self.angle = 0
		self.velocity = 0
		self.inertia = 1 # Prevents turning in place, makes things more realistic
		self.friction = 1 # Normal on road, 0.5 on grass

		self.maxSpeed = 25
		self.minSpeed = -10
		self.boost = 50.0

		self.drifting = 0
		self.momentum = 0

	def update_player(self, ground):
		# Check movement
		self.inertia = abs(self.velocity)/10
		if ground[1] >= GRASS:
			self.maxSpeed = 16
			if self.velocity > self.maxSpeed:
				self.velocity = self.maxSpeed
		else:
			self.maxSpeed = 25

		# Get new Location
		dX = cos(radians(self.angle)) * (self.velocity)
		dY = sin(radians(self.angle)) * (self.velocity)

		self.x += dX

		self.y += dY

		# Handle angle
		if self.angle >= 360:
			self.angle -= 360
		if self.angle < 0:
			self.angle += 360

		# Slow Down
		if self.velocity != 0:
			if self.velocity < 0:
				self.velocity +=1
			else:
				self.velocity -=1
		self.image, self.rect = rot_center(self.image_orig, self.rect, -self.angle)


	def handle_keys(self):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			# Rotate Left
			turn = -3 * self.inertia
			self.angle += turn * self.direction

		if key[pygame.K_RIGHT]:
			#Rotate right
			turn = 3 * self.inertia
			self.angle += turn * self.direction

		if key[pygame.K_UP]:
			if abs(self.velocity) < self.maxSpeed:
				self.velocity += 2
				self.direction = 1
		if key[pygame.K_DOWN]:
			if self.velocity > self.minSpeed:
				self.velocity -= 2
				self.direction = -1
		if key[pygame.K_LSHIFT]: # a sort of boost 
			if self.boost > 0:
				if self.maxSpeed <= 25:
					self.maxSpeed += 10
				self.boost -= 1
				if self.velocity < self.maxSpeed:
					self.velocity += 5
		else:
			self.maxSpeed = 25
			if self.boost < 50.0:
				self.boost += 0.3
		if key[pygame.K_SPACE]:
			# Handbrake
			
			if self.velocity > 0:
				self.velocity -= 5
			else:
				self.velocity += 5
		if key[pygame.K_LCTRL]:
			self.drifting = 1
			self.friction = 0.5
		else:
			self.drifting = 0
			self.friction = 1

	#	Creates a bar representing the level of boost remaining
	def boostBar(self):
		boost = pygame.Rect(pygame.display.Info().current_w - 200, pygame.display.Info().current_h - 75, self.boost * 3, 20)
		return boost

"""
	def draw(self, screen):
		surf = pygame.Surface((30, 15))
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

		self.position = screen.blit(rotatedSurf, rotRect)
		#screen.blit(rotImage, rotRect)
"""