import pygame
from settings import *

class Generador(pygame.sprite.Sprite):
    def __init__(self, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.bandera=True
        self.temp=random.randrange(100)

    def update(self):
        self.temp -= 1


class Generador2(pygame.sprite.Sprite):
    def __init__(self, pos, dim):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.bandera=True
        self.temp=random.randrange(100)

    def update(self):
        self.temp -= 1