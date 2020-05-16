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
        self.velx=0
        self.vely=0

    def update(self):
        if self.velx!=self.vely:
            if self.con < 8:
                self.con+=1
            else:
                self.con=0
        self.image=self.m[self.dir][self.con]
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self,pos,d_an,d_al, cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([d_an,d_al])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=0
