import pygame

class Highlight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        '''
        Defines the highlight box.
        param list:(object, int, int) needs xy coordinates
        return: (None)
        '''
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.image = pygame.Surface((140,140))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft=(self.x,self.y))

    def left(self):
        """
        moves the select rectangle to the left
        params: self
        returns: none
        """
        if self.rect.x > 50:
            self.rect.move_ip(-200,0)
        
    def right(self):
        """
        moves the select rectangle to the right
        params: self
        returns: none
        """
        if self.rect.x < 650:
            self.rect.move_ip(200,0)
        
