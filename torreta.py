import pygame
from settings import *

class Torreta(pygame.sprite.Sprite):
    def __init__(self, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.bandera=True
        self.temp=random.randrange(200)

    def RetPos(self):
        x=self.rect.x -10
        y=self.rect.y 
        return [x,y]

    def update(self):
        self.temp -= 1