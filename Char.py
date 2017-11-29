import pygame
import Highlight

WIDTH = 1000
HEIGHT = 700

class Char:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.list = ['steve2.png','colin3.png','melanie3.png','shania3.png','anthony3.png']
        self.first = pygame.image.load('steve2.png')
        self.second = pygame.image.load('colin3.png')
        self.third = pygame.image.load('melanie3.png')
        self.fourth = pygame.image.load('shania3.png')
        self.fifth = pygame.image.load('anthony3.png')
        self.first = pygame.transform.scale(self.first, (150,150))
        self.second = pygame.transform.scale(self.second, (150,150))
        self.third = pygame.transform.scale(self.third, (150,150))
        self.fourth = pygame.transform.scale(self.fourth, (150,150))
        self.fifth = pygame.transform.scale(self.fifth, (150,150))

        self.highlight = Highlight.Highlight(40,90)
        self.sprites = pygame.sprite.Group(self.highlight)
        self.choice = 'steve2.png'
        self.font = pygame.font.SysFont('lucidaconsole',27)
        self.fonty = pygame.font.SysFont('lucidaconsole',15)
        self.choose = self.fonty.render('Click Enter to choose your character',True,(0,255,255))
        self.instr = self.font.render('Instructions: Use the arrows keys to move your selected',True,(255,0,255))
        self.cont_one =self.font.render('character and push the spacebar to shoot the invading',True,(255,0,255))
        self.cont_two =self.font.render('Computer Scientists.',True,(255,0,255))
        self.mouse = pygame.mouse.get_pos()
        
    def start(self):
        self.display.blit(self.instr,(50,350))
        self.display.blit(self.cont_one,(100,400))
        self.display.blit(self.cont_two,(100,450))
        pygame.display.flip()
        letter = 'Click Enter to choose your character'
        self.x = 350
        for c in letter:
            self.text = self.fonty.render(c,True,(0,255,255))
            pygame.time.delay(50)
            self.display.blit(self.text,(self.x,600))
            self.background.blit(self.display,(self.x,600))
            self.x += 9
            pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.highlight.left()
                    elif event.key == pygame.K_RIGHT:
                        self.highlight.right()
                    elif event.key == pygame.K_RETURN:
                        if self.highlight.rect.x == 240:
                            self.choice = 'colin3.png'
                            del self.list[1]
                        elif self.highlight.rect.x == 440:
                            self.choice = 'melanie3.png'
                            del self.list[2]
                        elif self.highlight.rect.x == 640:
                            self.choice = 'shania3.png'
                            del self.list[3]
                        elif self.highlight.rect.x == 840:
                            self.choice = 'anthony3.png'
                            del self.list[4]
                        else:
                            del self.list[0]
                        return (self.choice,self.list)
                        done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 50<self.mouse[0]<170 and 100<self.mouse[1]<220:
                        self.highlight.rect.x = 40
                    elif pygame.mouse.get_pressed()[0] and 250<self.mouse[0]<370 and 100<self.mouse[1]<220:
                        self.highlight.rect.x = 240
                    elif pygame.mouse.get_pressed()[0] and 450<self.mouse[0]<570 and 100<self.mouse[1]<220:
                        self.highlight.rect.x = 440
                    elif pygame.mouse.get_pressed()[0] and 650<self.mouse[0]<770 and 100<self.mouse[1]<220:
                        self.highlight.rect.x = 640
                    elif pygame.mouse.get_pressed()[0] and 850<self.mouse[0]<970 and 100<self.mouse[1]<220:
                        self.highlight.rect.x = 840
                                                


            self.display.blit(self.background,(0,0))
            self.sprites.draw(self.display)
            self.display.blit(self.first,(40,90))
            self.display.blit(self.second,(240,90))
            self.display.blit(self.third,(440,90))
            self.display.blit(self.fourth,(640,90))
            self.display.blit(self.fifth,(840,90))
            self.display.blit(self.choose,(350,600))
            self.display.blit(self.instr,(50,350))
            self.display.blit(self.cont_one,(100,400))
            self.display.blit(self.cont_two,(100,450))
            pygame.display.flip()
        pygame.quit()
