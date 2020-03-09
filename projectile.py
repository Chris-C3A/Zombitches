import pygame

class Projectile(object):
    def __init__(self, x, y, facing, damage=25):
        self.x = x
        self.y = y
        self.radius = 3
        self.color = (255, 0, 0)
        self.facing = facing
        self.vel = 35
        self.damage = damage

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.x += self.vel * self.facing
    
    def collide(self, enemy):
        return self.x >= enemy.x and self.x <= enemy.x + enemy.w and self.y >= enemy.y and self.y <= enemy.y + enemy.h

# class Bullet(Projectile):
#     def __init__(self):