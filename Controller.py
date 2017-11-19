import pygame
import Bullet
import Ship
import Char
import Alien

WIDTH = 1000
HEIGHT = 700

class Controller:
    def __init__(self):
        pygame.init()
        self.x = WIDTH / 2
        self.y = HEIGHT - 140
        self.char = Char.Char()
        self.image = self.char.start()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.Surface(self.display.get_size()).convert()
        self.ship = Ship.Ship(self.image[0], self.x,self.y)
        #self.bullet = Bullet.Bullet(self.ship.x+60,self.ship.y)
        #print(pygame.font.get_fonts())
        self.alien_e= []
        self.alien_m = []
        self.alien_h =[]
        self.bullet = []
        self.easy =0
        self.medium = 20
        self.hard = 35
        self.mcount =0
        self.hcount =0
        self.alien_e.append(Alien.Alien(self.image[1]))
        #self.alien_m.append(Alien.Alien(self.image[1]))
        #self.alien_h.append(Alien.Alien(self.image[1]))
        self.sprites = pygame.sprite.Group((self. ship,)+ tuple(self.alien_e)+tuple(self.alien_m)+tuple(self.alien_h))

        #self.sprites = pygame.sprite.Group((self.bullet,) + tuple(self.alien))

    def start(self):
        move = [False,False]
        done = False
        while not done:
            make = True
            while make:                    
                if self.easy%2==0:
                    self.alien_e.append(Alien.Alien(self.image[1]))
                    if self.easy == self.medium:
                        self.alien_m.append(Alien.Alien(self.image[1]))
                    if self.easy == self.hard:
                        self.alien_h.append(Alien.Alien(self.image[1]))
                    self.easy += 1
                    break
                else:
                    self.easy +=1
                    break
            self.sprites = pygame.sprite.Group((self. ship,)+ tuple(self.alien_e)+tuple(self.alien_m)+tuple(self.alien_h))
            for a in range(len(self.alien_e)):
                while self.alien_e[a].rect.y<700:
                    pygame.time.delay(5)
                    self.alien_e[a].run()
                #while self.alien_e[a].rect.y<700 or self.alien_m[self.mcount].rect.y<700 or self.alien_h[self.hcount].rect.y<700:
                    #pygame.time.delay(5)
                    #while self.alien_e[a].rect.y<700:
                        #self.alien_e[a].run()
                        #break
                    #if self.easy == self.medium:
                        #if self.alien_m[self.mcount].rect.y<700:
                            #self.alien_m[self.mcount].run()
                    #self.alien_m[self.mcount+1].run()
                        #else:
                            #self.medium += 1
                            #self.mcount += 1
                    #if self.easy == self.hard:
                        #if self.alien_h[self.hcount].rect.y<700:
                            #self.alien_h[self.hcount].run()
                    #self.alien_m[self.mcount+1].run()
                        #else:
                            #self.hard += 1
                            #self.hcount += 1
                    self.display.blit(self.background,(0,0))
                    self.sprites.draw(self.display)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                move[0] = True
                            elif event.key == pygame.K_RIGHT:
                                move[1] = True
                            elif event.key == pygame.K_SPACE:
                                self.bullet.append(Bullet.Bullet(self.ship.rect.x+60,self.ship.rect.y))
                                self.sprites.add(self.bullet)
                            
                        elif event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT:
                                move[0] = False
                            elif event.key == pygame.K_RIGHT:
                                move[1] = False
                    if move[0]: 
                        self.ship.left()
                    elif move[1]:
                        self.ship.right()
                    for b in range(len(self.bullet)):
                        if self.bullet[b].rect.y>-20:
                            self.bullet[b].fire()
                        if self.bullet[b].rect.colliderect(self.alien_e[a].rect)and self.bullet[b].rect.y>65:
                            self.bullet[b].exit()
                            self.alien_e[a].exit()
                            self.bullet[b].kill()
                            self.alien_e[a].kill()
                            
                            self.display.blit(self.background,(0,0))
                            self.sprites.draw(self.display)
                            pygame.display.flip()
                        for m in range(len(self.alien_m)):
                            if self.bullet[b].rect.colliderect(self.alien_m[m].rect) and self.bullet[b].rect.y>65:
                                self.bullet[b].kill()
                                self.bullet[b].exit()
                                self.alien_m[m].exit()
                                self.display.blit(self.background,(0,0))
                                self.sprites.draw(self.display)
                                pygame.display.flip()
                        for h in range(len(self.alien_h)):
                            if self.bullet[b].rect.colliderect(self.alien_h[h].rect)and self.bullet[b].rect.y>65:
                                self.bullet[b].kill()
                                self.bullet[b].exit()
                                self.alien_h[h].exit()
                                self.display.blit(self.background,(0,0))
                                self.sprites.draw(self.display)
                                pygame.display.flip()
                    if self.ship.rect.colliderect(self.alien_e[a].rect):
                        return None
                    elif self.alien_e[a].rect.y ==640:
                        return None               


                        
            self.display.blit(self.background,(0,0))
            #self.sprites.draw(self.display)
            #self.display.blit(self.ship.image,(self.ship.rect.x,self.ship.rect.y))
            self.sprites.draw(self.display)
            pygame.display.flip()
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True

        pygame.quit()
