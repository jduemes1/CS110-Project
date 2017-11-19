import pygame
class bullet(pygame.sprite.Sprite):
    def __init__(self,speed):
        self.speed = speed
        self.image = pygame.surface((5,10))
    def shootBullet(self):
        self.y=0
        for i in range("""height of screen"""):
            self.y+=1
            if """collosion with alien""":
                """destroy alien"""
                """destroy itself"""
