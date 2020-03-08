import pygame
# from main import p_sprites

class Player(object):
    def __init__(self, x, y, w, h):
        self.x = x - w/2
        self.y = y - h/2
        self.w = w
        self.h = h
        self.vel = 15
        self.health = 100
        self.right = True
        self.left = False
        self.standing = True

        self.p_right = pygame.transform.scale(pygame.image.load("resources/player.png"), (100, 100))
        self.p_left = pygame.transform.flip(self.p_right, True, False) 

        # self.p_sprites = pygame.image.load("resources/player.png")
        # self.p_sprites = pygame.transform.scale(self.p_sprites, (100, 100))


    def draw(self, win):
        if not(self.standing):
            if self.left:
                win.blit(self.p_left, (self.x,self.y))
            elif self.right:
                win.blit(self.p_right, (self.x,self.y))
        else:
            if self.right:
                win.blit(self.p_right, (self.x, self.y))
            elif self.left:
                win.blit(self.p_left, (self.x, self.y))



