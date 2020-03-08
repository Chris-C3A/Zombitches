import pygame
import random

class Zombie(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100
        self.vel = random.randint(3, 7)
        self.walkcount = random.randint(0, 7)
        self.health = 100
        self.isDead = False

        self.z_sprites = []
        for i in range(8):
            self.z_sprites.append(pygame.image.load('resources/frame_' + str(i) + "_delay-0.1s.png"))
            self.z_sprites[i] = pygame.transform.scale(self.z_sprites[i], (self.w, self.h))
            self.z_sprites[i] = pygame.transform.flip(self.z_sprites[i], True, False)

        # font = pygame.font.Font('freesansbold.ttf', 10)
        # self.text = font.render("HP: " + str(self.health), True, (255, 0, 0))
        # self.textRect = self.text.get_rect()
        # self.textRect.center = (self.x + self.w/2, self.y)


    def draw(self, win):
        # win.blit(self.z_sprites[1], (self.x,self.y))
        self.x -= self.vel
        
        if self.walkcount == 7:
            self.walkcount = 0;

        self.walkcount += 1

        win.blit(self.z_sprites[self.walkcount], (self.x,self.y))

        # Health bar
        w, h = 50, 10
        pygame.draw.rect(win, (255,0,0),(self.x+w/2, self.y-h, w*(self.health/100), h), 0)
        # win.blit(self.text, (100, 100))