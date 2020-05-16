import pygame
from settings import *

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self,pos,d_an,d_al, cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([d_an,d_al])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=0
