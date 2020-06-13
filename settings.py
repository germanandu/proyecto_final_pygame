import pygame
import random

ANCHO=1024
ALTO=768
AMARILLO=[255,255,0]
AZUL=[0,0,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]

#velocidades
VELOCIDAD=3
VELOCIDAD_E=5
VELOCIDAD_G=2

WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768
TILESIZE = 64

#imagenes
personaje=pygame.image.load('img/personaje.png')
escorpion=pygame.image.load('img/escorpion.png')
bala=pygame.image.load('img/bala.png')
golem=pygame.image.load('img/golem.png')

fondo_inicio=pygame.image.load('img/fondo2.png')
congratulations=pygame.image.load('img/congratulations.png')
fondo_final=pygame.image.load('img/fondofinal.png')
titulo_inicio=pygame.image.load('img/titulo.png')
vida_j=pygame.image.load('img/vida.png')
vida_j2=pygame.image.load('img/vida2.png')
municion_i=pygame.image.load('img/municion.png')
rayo_i=pygame.image.load('img/rayo.png')
press_start=pygame.image.load('img/start.png')
cielo=pygame.image.load('img/cielo3.jpg')
gameover=pygame.image.load('img/gameover.png')
bola=pygame.image.load('img/bola.png')

temps=0

#recorte
m=[]
for f in range(4):
    fila=[]
    for c in range(9):
        cuadro=personaje.subsurface(64*c,64*f,64,64)
        fila.append(cuadro)
    m.append(fila)

m2=[]
for f in range(4):
    fila=[]
    for c in range(3):
        cuadro=escorpion.subsurface(64*c,64*f,64,64)
        fila.append(cuadro)
    m2.append(fila)

m3=[]
for c in range(4):
    cuadro=bala.subsurface(32*c,32*0,32,32)
    m3.append(cuadro)

m4=[]
for f in range(4):
    fila=[]
    for c in range(3):
        cuadro=golem.subsurface(64*c,80*f,64,80)
        fila.append(cuadro)
    m4.append(fila)

fin = False
gameover_b=False
colision=False
colision2=False
duracion_rayo=0
reloj=pygame.time.Clock()
#dt = reloj.tick(60) / 1000.0


