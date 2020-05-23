import pygame
from settings import *

class Escorpion(pygame.sprite.Sprite):
    def __init__(self, pos, m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.dir=0
        self.image=self.m[self.dir][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.obstaculos=None
        
    
    def update(self):
        if self.velx!=self.vely:
            if self.con < 2:
                self.con+=1
            else:
                self.con=0
        self.image=self.m[self.dir][self.con]
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Golem(pygame.sprite.Sprite):
    def __init__(self, pos, m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.dir=0
        self.image=self.m[self.dir][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.obstaculos=None
        self.vida=3
        self.temp=30
        
    
    def update(self):
        if self.velx!=self.vely:
            if self.con < 2:
                self.con+=1
            else:
                self.con=0
        self.image=self.m[self.dir][self.con]
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.temp-=1