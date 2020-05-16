import pygame
import random

ANCHO=1024
ALTO=768
AMARILLO=[255,255,0]
AZUL=[0,0,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]

VELOCIDAD=10

WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768
TILESIZE = 64

#imagenes
personaje=pygame.image.load('img/personaje.png')
#recorte
m=[]
for f in range(4):
    fila=[]
    for c in range(9):
        cuadro=personaje.subsurface(64*c,64*f,64,64)
        fila.append(cuadro)
    m.append(fila)

fin = False
reloj=pygame.time.Clock()
dt = reloj.tick(60) / 1000.0

#MAPA
