import pygame
import random
class aliens(pygame.sprite.Sprite):
    def __init__(self, pictures):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randrange(1001)
        self.y = 0
        self.pict = random.choice(pictures)
        self.image = pygame.image.load(self.pict)
        self.image = pygame.transform.scale(self.image, (65,65))
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
    def move(self, num =1):
        self.rect.y+=num
    def exit(self):
        self.rect.x = 1000
        self.rect.y = 700
