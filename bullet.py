import pygame
class bullet(pygame.sprite.Sprite):
    def __init__(self,xcoor,ycoor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((6,20))
        self.x = xcoor
        self.y = ycoor
        self.rect = self.image.get_rect(center = (self.x,self.y))
        
    def shootBullet(self):
        self.rect.y-=5
    def exit(self):
        self.rect.x = 1000
       
        
