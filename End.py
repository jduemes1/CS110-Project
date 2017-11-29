import pygame
import Controller
import json

WIDTH = 1000
HEIGHT = 700

class End:
    def __init__(self, num):
        '''
        Defines the end screen.
        param list:(object) only needs self
        return: (None)
        '''
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.bkground = pygame.image.load('Lab1.jpg')
        self.bkground = pygame.transform.scale(self.bkground,(1000,700))
        self.display.blit(self.bkground,(0,0))
        self.font = pygame.font.SysFont('lucidaconsole',50)
        self.fonty = pygame.font.SysFont('comicsansms',25)
        self.score = self.fonty.render('Your Score: ' + str(num),True,(0,255,0))

        self.file = json.loads(open('highscore.json').read())
        if num >= int(self.file['high']):
            diction = {'high' : num}
            write = json.dumps(diction)
            self.writefile = open('highscore.json', 'w')
            self.writefile.write(write)
            self.writefile.close()
            self.highscore = self.fonty.render('New High Score: ' + str(num),True,(0,255,0))
        else:
            self.highscore = self.fonty.render('High Score: ' + str(self.file['high']), True, (0,255,0))

        self.again = self.fonty.render('Try Again',True,(0,255,0))
        self.finish = self.fonty.render('Quit',True,(0,255,0))
        letter = 'Game Over'
        self.end = 300
        for c in letter:
            self.text = self.font.render(c,True,(255,0,0))
            pygame.time.delay(100)
            self.display.blit(self.text,(self.end,170))
            self.background.blit(self.display,(self.end,170))
            self.end += 50
            pygame.display.flip()
        self.display.blit(self.highscore,(370,250))
        self.display.blit(self.score,(400,320))
        pygame.draw.rect(self.display, (0,0,0),(560,500,140,40))
        pygame.draw.rect(self.display, (0,0,0),(560,550,70,40))
        self.display.blit(self.again,(560,500))
        self.display.blit(self.finish,(560,550))
        pygame.display.flip()
        self.mouse = pygame.mouse.get_pos()

        
    def choice(self):
        '''
        Runs the game over screen.
        param list:(object) only needs self
        return: (bool) returns True or False
        '''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse = pygame.mouse.get_pos()
                    if 560<self.mouse[0]<690 and 500<self.mouse[1]<540:
                        pygame.draw.rect(self.display, (255,255,255),(560,500,140,40))
                        self.display.blit(self.highscore,(370,250))
                        self.display.blit(self.score,(400,320))
                        self.display.blit(self.again,(560,500))
                        self.display.blit(self.finish,(560,550))
                        pygame.display.flip()

                    elif 555<self.mouse[0]<620 and 550<self.mouse[1]<590:
                        pygame.draw.rect(self.display, (255,255,255),(560,550,70,40))
                        self.display.blit(self.highscore,(370,250))
                        self.display.blit(self.score,(400,320))
                        self.display.blit(self.again,(560,500))
                        self.display.blit(self.finish,(560,550))
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(self.display, (0,0,0),(560,500,140,40))
                        pygame.draw.rect(self.display, (0,0,0),(560,550,70,40))
                        self.display.blit(self.highscore,(370,250))
                        self.display.blit(self.score,(400,320))
                        self.display.blit(self.again,(560,500))
                        self.display.blit(self.finish,(560,550))
                        pygame.display.flip()
                                                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and 560<self.mouse[0]<690 and 500<self.mouse[1]<540:
                        return True
                    elif pygame.mouse.get_pressed()[0] and 560<self.mouse[0]<620 and 550<self.mouse[1]<590:
                        return False
            pygame.display.flip()
    def close(self):
        '''
        Closes screen.
        param list:(object) only needs self
        return: (None)
        '''
        pygame.quit()
