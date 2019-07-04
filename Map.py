import pygame
map_files = []
map_tiles = ['X_Road.png', 'I_Road.png', 'L_Road.png', 'T_Road.png', 'E_Road.png', 'Grass.png']
X = 0
I = 1
L = 2
T = 3
E = 4
G = 5

map_1 = [
          [2,1,3,1,1,3,1,1,1,4],
          [1,5,1,5,4,0,1,2,5,4],
          [1,4,3,1,3,3,1,3,2,1],
          [3,1,3,1,3,5,4,5,1,1],
          [3,2,1,5,1,5,3,1,0,3],
          [1,2,0,1,0,3,0,4,1,1],
          [1,5,1,4,2,1,1,2,3,1],
          [1,2,0,1,3,3,0,0,2,1],
          [1,1,4,2,2,5,1,2,1,3],
          [2,3,1,3,1,1,3,1,1,2]
        ]

#tilemap rotation, x90ccw
map_1_rot = [
          [1,0,1,0,0,1,0,0,0,2],
          [1,0,1,0,0,0,0,2,0,3],
          [1,0,3,0,1,3,0,3,2,1],
          [0,0,1,0,2,0,3,0,1,1],
          [0,2,1,0,1,0,0,0,0,1],
          [1,0,0,0,0,1,0,2,1,2],
          [1,0,1,0,3,1,1,1,2,1],
          [1,1,0,0,1,3,0,0,3,1],
          [1,1,3,1,3,0,1,0,0,1],
          [0,3,0,3,0,0,3,0,0,3]
        ]


class Map(pygame.sprite.Sprite):
    def __init__(self, tile_map, x, y, rot):
        pygame.sprite.Sprite.__init__(self)
        self.image = map_files[tile_map]
        self.rect = self.image.get_rect()

        if rot != 0:
            self.image = pygame.transform.rotate(self.image, rot * 90)

        self.x = x
        self.y = y 

    #Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y
