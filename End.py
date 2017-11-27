import pygame
import Controller

WIDTH = 1000
HEIGHT = 700

class End:
    def __init__(self, num):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.font = pygame.font.SysFont('lucidaconsole',50)
        self.fonty = pygame.font.SysFont('comicsansms',30)
        self.score = self.fonty.render('Your Score: ' + str(num),True,(0,255,0)) 
        self.again = self.fonty.render('Try Again',True,(0,255,0))
        self.finish = self.fonty.render('Quit',True,(0,255,0))
        letter = 'Game Over'
        self.end = 300
        for c in letter:
            self.text = self.font.render(c,True,(255,0,0))
            pygame.time.delay(100)
            self.display.blit(self.text,(self.end,200))
            self.background.blit(self.display,(self.end,200))
            self.end += 50
            pygame.display.flip()
        self.display.blit(self.score,(400,350))
        self.display.blit(self.again,(360,500))
        self.display.blit(self.finish,(360,550))
        pygame.display.flip()
        self.mouse = pygame.mouse.get_pos()

        
    def choice(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse = pygame.mouse.get_pos()
                    #print(self.mouse)
                    if 360<self.mouse[0]<490 and 500<self.mouse[1]<540:
                        pygame.draw.rect(self.display, (255,255,255),(360,500,140,40))
                        self.display.blit(self.score,(400,350))
                        self.display.blit(self.again,(360,500))
                        self.display.blit(self.finish,(360,550))
                        pygame.display.flip()

                    elif 355<self.mouse[0]<420 and 550<self.mouse[1]<590:
                        pygame.draw.rect(self.display, (255,255,255),(360,550,70,40))
                        self.display.blit(self.score,(400,350))
                        self.display.blit(self.again,(360,500))
                        self.display.blit(self.finish,(360,550))
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(self.display, (0,0,0),(360,500,160,50))
                        pygame.draw.rect(self.display, (0,0,0),(360,550,70,50))
                        self.display.blit(self.score,(400,350))
                        self.display.blit(self.again,(360,500))
                        self.display.blit(self.finish,(360,550))
                        pygame.display.flip()
                                                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #self.mouse = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and 360<self.mouse[0]<490 and 500<self.mouse[1]<540:
                        return True
                    elif pygame.mouse.get_pressed()[0] and 360<self.mouse[0]<420 and 550<self.mouse[1]<590:
                        return False
            pygame.display.flip()
    def close(self):
        pygame.quit()
