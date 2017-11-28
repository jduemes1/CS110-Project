import pygame
import bullet
import ship
import Char
import aliens
import score

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
        self.room = pygame.image.load('classroom2.jpg')
        self.room = pygame.transform.scale(self.room,(1000,700))
        self.background.blit(self.room,(0,0))
        self.ship = ship.ship(self.image[0], self.x,self.y)
        #print(pygame.font.get_fonts())
        self.alien= []
        self.bullet = []
        self.num =0
        self.speed = 1
        self.spriteship = pygame.sprite.Group(self.ship)
        self.spritealien = pygame.sprite.Group(self.alien)
        self.spritebullet = pygame.sprite.Group(self.bullet)

        self.font = pygame.font.SysFont('bodoniblack',30)
        self.score = score.score()
        self.value = self.font.render('Score: '+ str(self.score.count),True,(0,255,0))
        
    def start(self):
        move = [False,False]
        done = False
        while not done:
            self.alien.append(aliens.aliens(self.image[1]))
            self.spritealien.add(self.alien)
            if len(self.alien)%15 == 0:
                self.speed += 1
            for a in range(len(self.alien)):
                while self.alien[a].rect.y<700:
                    pygame.time.delay(5)
                    self.alien[a].move(self.speed)
                    self.display.blit(self.background,(0,0))
                    self.spriteship.draw(self.display)
                    self.spritealien.draw(self.display)
                    self.spritebullet.draw(self.display)
                    #self.sprites.draw(self.display)
                    self.display.blit(self.value,(30,30))
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
                                self.bullet.append(bullet.bullet(self.ship.rect.x+60,self.ship.rect.y))
                                self.spritebullet.add(self.bullet)
                            
                        elif event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT:
                                move[0] = False
                            elif event.key == pygame.K_RIGHT:
                                move[1] = False
                    if move[0]: 
                        self.ship.moveLeft(self.speed)
                    elif move[1]:
                        self.ship.moveRight(self.speed)
                    #for collide in self.sprites:
                        #pygame.sprite.spritecollide(collide,
                        
                    for b in range(len(self.bullet)):
                        if self.bullet[b].rect.y>-20:
                            self.bullet[b].shootBullet()
                        if self.bullet[b].rect.colliderect(self.alien[a].rect)and self.bullet[b].rect.y>65:
                            self.bullet[b].kill()
                            self.alien[a].kill()
                            self.bullet[b].exit()
                            self.alien[a].exit()
                            
                            self.score.increase()
                            self.value = self.font.render('Score: '+ str(self.score.count),True,(0,255,0))

                            #self.sprites.update()
                            #self.sprites.draw(self.display)
                            self.spriteship.draw(self.display)
                            self.spritealien.draw(self.display)
                            self.spritebullet.draw(self.display)
                            pygame.display.flip()
                    if self.ship.rect.colliderect(self.alien[a].rect):
                        return self.score.count
                    elif 640 <= self.alien[a].rect.y <=700:
                        return self.score.count               


            self.display.blit(self.background,(0,0))
            self.spriteship.draw(self.display)
            self.spritealien.draw(self.display)
            self.spritebullet.draw(self.display)
            #self.sprites.draw(self.display)
            self.display.blit(self.value,(30,30))
            pygame.display.flip()
            for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True

        pygame.quit()
