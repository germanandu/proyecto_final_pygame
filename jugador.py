import pygame
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
        self.obstaculos=None
        self.vida=4
        self.score=0
        self.balas=25
    
    def RetPos(self):
        x=self.rect.x +34
        y=self.rect.y +24
        return [x,y]

    def update(self):
        if self.velx!=self.vely:
            if self.con < 8:
                self.con+=1
            else:
                self.con=0
        self.image=self.m[self.dir][self.con]
        self.rect.x+=self.velx
        ls_col=pygame.sprite.spritecollide(self,self.obstaculos,False)
        #Colision  en X
        for b in ls_col:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right= b.rect.left
                    self.velx=0
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left= b.rect.right
                    self.velx=0
        #Colision en Y
        self.rect.y+=self.vely
        ls_col=pygame.sprite.spritecollide(self,self.obstaculos,False)
        for b in ls_col:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom= b.rect.top
                    self.vely=0
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top= b.rect.bottom
                    self.vely=0