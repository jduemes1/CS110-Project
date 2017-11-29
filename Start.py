import pygame

WIDTH = 1000
HEIGHT = 700

class Start:
    def __init__(self):
        '''
        Defines the start screen.
        param list:(object) only needs self
        return: (None)
        '''
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.font = pygame.font.SysFont('comicsansms',30)
        self.fonty = pygame.font.SysFont('lucidaconsole',70)
        self.play = self.font.render('Play',True,(0,255,0))
        self.display.blit(self.play,(400,500))
        
        self.bkground = pygame.image.load('clocktower.jpg')
        self.bkground = pygame.transform.scale(self.bkground,(1000,700))
        self.display.blit(self.bkground,(0,0))
        pygame.draw.rect(self.display, (0,0,0),(400,500,70,45))
        self.display.blit(self.play,(400,500))
        pygame.display.flip()
        
        self.mouse = pygame.mouse.get_pos()
        letter = 'Comp Sci Invaders'
        self.x = 150
        for c in letter:
            self.text = self.fonty.render(c,True,(0,0,255))
            pygame.time.delay(50)
            self.display.blit(self.text,(self.x,200))
            self.background.blit(self.display,(self.x,350))
            self.x += 40
            pygame.display.flip()

        
    def choice(self):
        '''
        Runs the start screen and the play button.
        param list:(object) only needs self
        return: (bool) returns True if play button clicked
        '''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse = pygame.mouse.get_pos()
                    if 400<self.mouse[0]<470 and 500<self.mouse[1]<540:
                        pygame.draw.rect(self.display, (255,255,255),(400,500,70,45))
                        self.display.blit(self.play,(400,500))
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(self.display, (0,0,0),(400,500,70,45))
                        self.display.blit(self.play,(400,500))
                        pygame.display.flip()
                                                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and 400<self.mouse[0]<470 and 500<self.mouse[1]<550:
                        return True
            pygame.display.flip()
        pygame.quit()
