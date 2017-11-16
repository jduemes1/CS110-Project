import pygame
class ship:
    def __init__(self, image: str):
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        #angle of gun
    def moveRight(self):
        self.rect.x += 1
class bullet:
    def __init(self,speed):
        self.speed = speed
class aliens:
    def __init__(self,speed):
        self.speed = speed
    def moveDown(self):
class controller:
    def __init__(self):
        self.speedUp
class score:
    def __init__(self):
        self.accum = 0
        
