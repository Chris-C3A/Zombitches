#!/usr/bin/env python3
import pygame
import sys
from pygame.locals import *
import random
import numpy as np
import time
# from src import player, zombie
import player
import zombie
import projectile

pygame.init()

blackspace = 80
indent = 20
screen = (1280, 720+blackspace)

# font = pygame.font.SysFont("comicsansms", 72)

clock = pygame.time.Clock()
win = pygame.display.set_mode(screen)

bg = pygame.image.load("resources/background.jpg")

pygame.display.set_caption('Zombitches 1.0')

zombies = []
# positions = [0+blackspace, 120+blackspace, 120*2, 120*3, 120*4, 120*5, 120*6]
positions = []
for i in range(6):
    positions.append(120*i + blackspace + indent)

# for i in range(6):
#     zombies.append(zombie.Zombie(screen[0] + 150, positions[i]))

p1 = player.Player(200, screen[1]/2, 100, 100)

bullets = []


def redrawGameWindow():
    win.blit(bg, (0,0+blackspace))

    p1.draw(win)

    for zm in zombies:
        zm.draw(win)
        if zm.x < 0 or zm.health <= 0:
            zombies.pop(zombies.index(zm))

    for bullet in bullets:
        bullet.draw(win)
        if bullet.x > screen[0] or bullet.x < 0:
            bullets.pop(bullets.index(bullet))

    # handling collision
    for bullet in bullets:
        for zm in zombies:
            if bullet.collide(zm):
                # TODO remove item from list in reverse order
                # bug here
                bullets.pop(bullets.index(bullet))
                zm.health -= 25

    # for i in range(len(bullets)-1):
    #     for j in range(len(zombies)-1):
    #         if bullets[i].collide(zombies[j]):
    #             bullets.pop(i)
    #             zombies[j].health -= 25
    
    pygame.display.update()


def eventHandling():
    x,y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            facing = 0
            if p1.right:
                facing = 1
            elif p1.left:
                facing = -1

            bullets.append(projectile.Projectile(int(p1.x + p1.w/2), int(p1.y + p1.h/2), facing))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and p1.x > 0:
        p1.x -= p1.vel
        # p1.left = True
        # p1.right = False
        p1.standing = False
    elif keys[pygame.K_RIGHT] and p1.x < screen[0] - p1.w - p1.vel:
        p1.x += p1.vel
        # p1.left = False
        # p1.right = True
        p1.standing = False
    else:
        p1.standing = True

    if keys[pygame.K_UP] and p1.y > 0+blackspace:
        p1.y -= p1.vel
    elif keys[pygame.K_DOWN] and p1.y < screen[1]- p1.h - p1.vel:
        p1.y += p1.vel

def main():
    wave = 0
    while True:
        clock.tick(14)

        if len(zombies) == 0:
            wave += 1
            for i in range(wave*2+4):
                zombies.append(zombie.Zombie(screen[0] + 150, random.choice(positions)))

        eventHandling()
        redrawGameWindow()

if __name__ == "__main__":
    main()
