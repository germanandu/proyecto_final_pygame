
from settings import *
from tilemap import *
from jugador import *
from obstaculo import *
from os import path
import pygame


if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    #GRUPOS
    jugadores=pygame.sprite.Group()
    obstaculos=pygame.sprite.Group()
    #CREACION OBJETOS
    #j=Jugador([128,66],m)
    #jugadores.add(j)
    #JUEGO
    #game_folder = path.dirname(__file__)
    #map_folder = path.join(game_folder, 'maps')
    #map = TiledMap(path.join(map_folder, 'level1.tmx'))

    map = TiledMap('maps/mapa2.tmx')
    map_img = map.make_map()
    map_rect = map_img.get_rect()
    camara = Camara(map.width,  map.height)

#CREACION  OBSTACULOS
    for tile_object in map.tmxdata.objects:

        if tile_object.name == 'player':
            j = Jugador([tile_object.x, tile_object.y],m)
            jugadores.add(j)
        if tile_object.name == 'wall':
            o=Obstaculo([tile_object.x, tile_object.y],tile_object.width, tile_object.height)
            obstaculos.add(o)
    j.obstaculos=obstaculos

    while not fin:
        #gestion de eventos---------------------------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True

            j.velx, j.vely = 0, 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                j.dir=1
                j.velx=-VELOCIDAD
                j.vely=0
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                j.dir=3
                j.velx=VELOCIDAD
                j.vely=0
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                j.dir=0
                j.velx=0
                j.vely=-VELOCIDAD
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                j.dir=2
                j.velx=0
                j.vely=VELOCIDAD



        #REFRESCO
        #ventana.fill(NEGRO)
        camara.update(j)
        jugadores.update()
        ventana.blit(map_img, camara.apply_rect(map_rect))
        ventana.blit(j.image,camara.apply(j))
        pygame.display.flip()
        reloj.tick(60)
