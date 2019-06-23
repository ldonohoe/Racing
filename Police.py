import random

def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

class Police(pygame.sprite.Sprite):

	def __init__(self):
		self.image = pygame.image.load('police_car.png')
		colorkey = self.image.get_at((0,0))
		self.image.set_colorkey(colorkey, RLEACCEL)
		self.image_orig = self.image
		self.x = 0
		self.y = 0
		self.target = None
		self.direction = 0
		self.rect = self.image.get_rect()
		self.velocity = 0
		self.angle = 0
		self.inertia = 1
	#	Updates the police's location, if it is after a target,
	#	
	def update(self, target):
		# Check movement
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
