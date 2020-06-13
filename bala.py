import pygame
from settings import *

class Bala(pygame.sprite.Sprite):
    def __init__(self, pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.dir=0
        self.image=self.m[self.dir]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=0
        self.velx=0

    def update(self):
        if self.velx!=self.vely:
            if self.con < 3:
                self.con+=1
            else:
                self.con=0
        self.image=self.m[self.dir]
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Bala2(pygame.sprite.Sprite):
    def __init__(self, pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.image=m
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=0

    def update(self):
        self.rect.y+=self.vely
        