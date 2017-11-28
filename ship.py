import pygame
class ship(pygame.sprite.Sprite):
    def __init__(self, image: str, xcoor, ycoor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(120,120))
        self.rect = self.image.get_rect(topleft = (xcoor, ycoor))
        self.x = xcoor
        self.y = ycoor
    def moveRight(self, speed):
        if self.rect.x < 930: 
            self.x+=speed +2 
    def moveLeft(self,speed):
        if self.rect.x >-50:
            self.x-=speed+ 2
            
     
