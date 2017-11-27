import pygame
import Image
import Highlight

WIDTH = 1000
HEIGHT = 700

class Char:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.list = ['steve2.png','colin3.png','melanie3.png','shania3.png','anthony3.png']
        self.first = Image.Image('steve2.png')
        self.second = Image.Image('colin3.png')
        self.third = Image.Image('melanie3.png')
        self.fourth = Image.Image('shania3.png')
        self.fifth = Image.Image('anthony3.png')
        self.highlight = Highlight.Highlight(40,90)
        self.sprites = pygame.sprite.Group(self.highlight)
        self.choice = 'steve2.png'
        self.font = pygame.font.SysFont('lucidaconsole',25)
        self.choose = self.font.render('Click Enter to choose your character',True,(0,255,255))
        self.instr = self.font.render('Instructions: Use the arrows keys to move your selected',True,(255,0,255))
        self.cont_one =self.font.render('character and push the spacebar to shoot the invading',True,(255,0,255))
        self.cont_two =self.font.render('Computer Scientists.',True,(255,0,255))
        self.mouse = pygame.mouse.get_pos()
        
    def start(self):
        letter = 'Click Enter to choose your character'
        self.x = 200
        for c in letter:
            self.text = self.font.render(c,True,(0,255,255))
            pygame.time.delay(50)
            self.display.blit(self.text,(self.x,350))
            self.background.blit(self.display,(self.x,350))
            self.x += 15
            pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.highlight.left()
                        #print(self.highlight.rect.x)
                    elif event.key == pygame.K_RIGHT:
                        self.highlight.right()
                        #print(self.highlight.rect.x)
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
                    #print(self.mouse)
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
            self.display.blit(self.first.image,(40,90))
            self.display.blit(self.second.image,(240,90))
            self.display.blit(self.third.image,(440,90))
            self.display.blit(self.fourth.image,(640,90))
            self.display.blit(self.fifth.image,(840,90))
            self.display.blit(self.choose,(200,350))
            self.display.blit(self.instr,(100,500))
            self.display.blit(self.cont_one,(150,550))
            self.display.blit(self.cont_two,(150,600))
            pygame.display.flip()
        pygame.quit()
