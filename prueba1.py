import pygame
import random
from settings import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos, m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.dir=2
        self.image=self.m[self.dir][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vx, self.vy = 0, 0
        self.x = pos[0] * TILESIZE
        self.y = pos[1] * TILESIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -VELOCIDAD
            self.dir=1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = VELOCIDAD
            self.dir=3
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -VELOCIDAD
            self.dir=0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = VELOCIDAD
            self.dir=2

        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def update(self):

        if self.vx!=self.vy:
            if self.con < 8:
                self.con+=1
            else:
                self.con=0
        self.image=self.m[self.dir][self.con]

        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rect.x = self.x
        self.rect.y = self.y
