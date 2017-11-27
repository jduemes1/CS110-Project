import pygame

class Highlight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.image = pygame.Surface((140,140))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft=(self.x,self.y))

    def left(self):
        if self.rect.x > 50:
            self.rect.move_ip(-200,0)
        
    def right(self):
        if self.rect.x < 650:
            self.rect.move_ip(200,0)
        
