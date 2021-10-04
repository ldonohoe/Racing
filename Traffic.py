import random, pygame, Map
from pygame.locals import *
from random import *
from math import *


car_files = ['red_car.png', 'green_car.png', 'black_car.png', 'purple_car.png', 'orange_car.png']
cars = []

GRASS = 230
CENTERW = -1
CENTERH = -1
DIRECTIONS = [0, 90, 180, 270]
SCREEN = None



def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def initTraf(centerW, centerH):
	CENTERW = centerW
	CENTERH = centerH

class Traffic(pygame.sprite.Sprite):

	def getSpawn(self, x=-1, y=-1):
		# Get random coordinates in the map tiles

		x = x if x > 0 else randint(0, 9)
		y = y if y > 0 else randint(0, 9)

		while(Map.map_1[x][y] == 5):
			x = randint(0, 9)
			y = randint(0, 9)

		print("Traffic Spawn: ", (x,y))

		return (x * 1000) + 500, (y * 1000) + 500


	def getTile(self):

		try:
			return Map.map_1[int((self.y + CENTERH) / 1000)][int((self.x + CENTERW) / 1000)]

		except:
			return -1


	def update(self, x, y):
		self.drive(self.getTile())
		self.inertia = abs(self.velocity)/10

		# Get new Location
		dX = cos(radians(self.angle)) * self.velocity
		dY = sin(radians(self.angle)) * self.velocity


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

		self.rect.topleft = self.x-x, self.y-y


	def drive(self, tile):
		# Check for a destination, get a new one if none

		# Pathfind to destination

		# Follow path
		#print(self.tile)
		if self.tile != self.getTile(): # Driven into a new tile, change goal direction, update own tile
			print(f"New Tile: {self.getTile()}")
			self.goalAngle = self.path.pop()
			self.tile = self.getTile()
		# Otherwise, continue driving through current tile
		angle_dif = self.angle - self.goalAngle
		if angle_dif > 3:
			self.angle -= 2
		elif angle_dif < -3:
			self.angle += 2
		accel = randint(0, 3)
		if randint(0, 10) > 9:
			accel = -accel
		if self.velocity < self.maxSpeed:
			self.velocity += accel

	def getDest(self):
		# Get random coordinates in the map tiles
		x = randint(0, 9)
		y = randint(0, 9)

		while(Map.map_1[x][y] != 4):
			x = randint(0, 9)
			y = randint(0, 9)

		print((x,y))

		return (x,y)



	def __init__(self, spawn=None):
		pygame.sprite.Sprite.__init__(self)
		carNum = randint(0, 4)
		self.image = pygame.image.load('resources/' + car_files[carNum])
		colorkey = self.image.get_at((0,0))
		self.image.set_colorkey(colorkey, RLEACCEL)
		self.image_orig = self.image
		self.screen = pygame.display.get_surface()
		self.area = self.screen.get_rect()
		if spawn:
			self.x, self.y = spawn
		else:
			self.x, self.y = self.getSpawn()
		self.direction = 0
		self.velocity = randint(1, 10)
		self.rect = self.image.get_rect()
		self.rect.topleft = self.x, self.y
		self.angle = 0
		self.inertia = 1
		self.destination = self.getDest()
		self.maxSpeed = randint(10, 20)
		self.tile = self.getTile()

		self.path = [0, 90, 0, 180, 0, 90, 0, 0, 0, 90, 180, 90, 180, 38] # List of directions to get to destination
		self.goalAngle = self.path[0]

