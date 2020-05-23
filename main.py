
from settings import *
from tilemap import *
from generador import *
from enemigos import *
from bala import *
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
    escorpiones=pygame.sprite.Group()
    generadores=pygame.sprite.Group()
    generadores2=pygame.sprite.Group()
    golems=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    arenas=pygame.sprite.Group()
    lavas=pygame.sprite.Group()
    #PANTALLA DE INICIO

    inicio_juego=False
    fin_juego=False
    #INICIO MUSICA
    msc_inicio=pygame.mixer.Sound('music/Battleship.ogg')
    ambiente=pygame.mixer.Sound('music/ambiente.wav')
    caminar=pygame.mixer.Sound('music/caminando_pasto.wav')
    disparo=pygame.mixer.Sound('music/disparo.wav')
    scorem=pygame.mixer.Sound('music/score.wav')
    impacto=pygame.mixer.Sound('music/impacto.wav')
    hurt=pygame.mixer.Sound('music/hurt.wav')

    msc_inicio.play()

    while (not fin) and (not inicio_juego):
        #GESTION DE EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    inicio_juego=True
        #ventana.blit(cielo,[0,0])
        ventana.blit(fondo_inicio,[0,-100])
        ventana.blit(titulo_inicio,[200,300])
        ventana.blit(press_start,[350,600])
        pygame.display.flip()
    msc_inicio.stop()
    #LETRAS
    score=pygame.font.SysFont("Times New Roman, Arial",30)
    fuente_j=pygame.font.SysFont("Times New Roman, Arial",30)
    balas_f=pygame.font.SysFont("Times New Roman, Arial",30)
    
    #CREACION DEL MAPA
    map = TiledMap('maps/mapa2.tmx')
    map_img = map.make_map()
    map_rect = map_img.get_rect()
    camara = Camara(map.width,  map.height)

#CREACION  OBSTACULOS Y CLASES
    for tile_object in map.tmxdata.objects:

        if tile_object.name == 'player':
            j = Jugador([tile_object.x, tile_object.y],m)
            jugadores.add(j)
        if tile_object.name == 'wall':
            o=Obstaculo([tile_object.x, tile_object.y],tile_object.width, tile_object.height)
            obstaculos.add(o)
        if tile_object.name == 'arena':
            a=Arena([tile_object.x, tile_object.y],tile_object.width, tile_object.height)
            arenas.add(a)
        if tile_object.name == 'lava':
            l=Lava([tile_object.x, tile_object.y],tile_object.width, tile_object.height)
            lavas.add(l)
        if tile_object.name == 'generador':
            g=Generador([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            generadores.add(g)
        if tile_object.name == 'generador2':
            g=Generador2([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            generadores2.add(g)
    j.obstaculos=obstaculos

    ambiente.play()
    while not fin:

        #GESTION DE EVENTOS
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if j.balas > 0:
                    disparo.play()
                    if j.dir==3:
                        p=j.RetPos()
                        b=Bala(p,m3)
                        b.velx= 10
                        b.dir=0
                    if j.dir==1:
                        p=j.RetPos()
                        b=Bala(p,m3)
                        b.velx= -10
                        b.dir=2
                    if j.dir==0:
                        p=j.RetPos()
                        b=Bala(p,m3)
                        b.vely= -10
                        b.dir=1
                    if j.dir==2:
                        p=j.RetPos()
                        b=Bala(p,m3)
                        b.vely= 10
                        b.dir=3
                    balas.add(b)
                    j.balas -= 1
                    

        #GENERA ESCORPIONES Y GOLEMS
        for g in generadores:
            if g.bandera==True and g.temp < 0:
                g.temp=random.randrange(100)
                e=Escorpion([g.rect.x -30, g.rect.y],m2)
                escorpiones.add(e)
                e.vely=VELOCIDAD_E
                g.bandera=False

        for g in generadores2:
            if g.bandera==True and g.temp < 0:
                g.temp=random.randrange(100)
                g1=Golem([g.rect.x -30, g.rect.y],m4)
                golems.add(g1)
                g1.vely=VELOCIDAD_G
                g.bandera=False
        
        #LIMITACION DE MOVIMIENTO ENEMIGOS
        for e in escorpiones:
            ls_l=pygame.sprite.spritecollide(e,obstaculos,False)
            for l in ls_l:
                if e.dir==0:
                    e.vely= -VELOCIDAD_E
                    e.dir=3
                elif e.dir==3:
                    e.vely= VELOCIDAD_E
                    e.dir=0
        
        for g in golems:
            ls_l=pygame.sprite.spritecollide(g,obstaculos,False)
            for l in ls_l:
                if g.dir==0:
                    g.vely= -VELOCIDAD_G
                    g.dir=3
                elif g.dir==3:
                    g.vely= VELOCIDAD_G
                    g.dir=0
        
        #JUGADOR
        ls_l=pygame.sprite.spritecollide(j,escorpiones,False)
        for l in ls_l:
            if temps < 0:
                j.vida -= 1
                hurt.play()
                temps=60
        
        ls_l1=pygame.sprite.spritecollide(j,golems,False)
        for l in ls_l1:
            if temps < 0:
                j.vida -= 1
                hurt.play()
                temps=60
        
        ls_l2=pygame.sprite.spritecollide(j,arenas,False)
        for l in ls_l2:
            colision=True
        if colision:
            VELOCIDAD=1
            colision=False
        else: VELOCIDAD=3

        ls_l3=pygame.sprite.spritecollide(j,lavas,False)
        for l in ls_l3:
            if temps < 0:
                j.vida -= 1
                hurt.play()
                temps=60

                

        #BALAS
        for b in balas:
            #ELIMINAR ESCORPION GOLPEANDO POR BALA
            ls_l=pygame.sprite.spritecollide(b,escorpiones,False)
            for e in ls_l:
                escorpiones.remove(e)
                j.score += 1000
                scorem.play()
                balas.remove(b)
            #ELIMINAR GOLEM GOLPEANDO POR BALA
            ls_l2=pygame.sprite.spritecollide(b,golems,False)
            for g in ls_l2:
                if g.temp < 0:
                    g.vida-=1
                    g.temp=30
                    balas.remove(b)
                    if g.vida==0:
                        golems.remove(g)
                        j.score += 1000
                        scorem.play()
                        
            #ELIMINAR BALA AL CHOCAR CON UN OBSTACULO
            ls_l1=pygame.sprite.spritecollide(b,obstaculos,False)
            for x in ls_l1:
                balas.remove(b)
                impacto.play()
                

        #REFRESCO
        msj='VIDAS='+str(j.vida)
        msj2='SCORE='+str(j.score)
        msj3='BALAS='+str(j.balas)+'/25'
        info=fuente_j.render(msj,True,BLANCO)
        info2=score.render(msj2,True,BLANCO)
        info3=balas_f.render(msj3,True,BLANCO)
        balas.update()
        generadores.update()
        generadores2.update()
        golems.update()
        escorpiones.update()
        camara.update(j)
        jugadores.update()
        ventana.blit(map_img, camara.apply_rect(map_rect))
        ventana.blit(j.image,camara.apply(j))
        for e in escorpiones:
            ventana.blit(e.image,camara.apply(e))
        for b in balas:
            ventana.blit(b.image,camara.apply(b))
        for g in golems:
            ventana.blit(g.image,camara.apply(g))
        #INFO JUEGO
        ventana.blit(info,[10,0])
        ventana.blit(info2,[300,0])
        ventana.blit(info3,[700,0])
        
        #escorpiones.draw(ventana)
        pygame.display.flip()
        #TEMPORIZADOR
        temps -= 1
        reloj.tick(60)
