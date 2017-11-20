import pygame
class ship:
    def __init__(self, image: str, xcoor, ycoor):
        self.image = pygame.image.load("Path")
        self.x = xcoor
        self.y = ycoor
    def moveRight(self):
        self.x += 1
    def moveLeft(self):
        self.x -= 1
