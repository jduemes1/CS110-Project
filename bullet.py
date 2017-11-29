import pygame
class bullet(pygame.sprite.Sprite):
    def __init__(self,xcoor,ycoor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((6,20))
        self.image.fill((255,0,0))
        self.x = xcoor
        self.y = ycoor
        self.rect = self.image.get_rect(center = (self.x,self.y))
        
    def shootBullet(self):
        """
        shoots the bullet
        params: none
        returns: none
        """
        self.rect.y-=5
    def exit(self):
        self.rect.x = 1050
       
        
