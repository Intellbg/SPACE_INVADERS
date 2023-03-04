import pygame
import sys
from sprites.misil import Misil

from sprites.naves.nave_defensora import NaveDefensora

pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 563

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#PANTALLA DE PAUSA------------------------------------------------------------------------
font = pygame.font.Font(None, 70)

text_surfacePausa = font.render("PAUSA", True, (255, 0, 128))
text_pausa = text_surfacePausa.get_rect()
text_pausa.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

text_surfaceR = font.render("Presiona la tecla R para continuar", True, (255, 177, 187))
text_R = text_surfaceR.get_rect()
text_R.center = (SCREEN_WIDTH // 2  , SCREEN_HEIGHT // 2 + 50)

#----------------------------------------------------------------------------------------

pygame.display.set_caption("SPACE INVADERS")

running = True
final = True

clock = pygame.time.Clock()
        
jugador = NaveDefensora(SCREEN_WIDTH,SCREEN_HEIGHT)
velocidadNave = 0
misil = None



#Funcion pausar()
def pausar():
    global running
    pausa = True
    while pausa:
        #Imprimir mensaje en pantalla------------
        screen.blit(text_surfacePausa, text_pausa)
        screen.blit(text_surfaceR, text_R)
        pygame.display.update()
        #----------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pausa = False
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
                pausa = False 
        



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                misil=jugador.shoot()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jugador.moveX(-1)
    if keys[pygame.K_RIGHT]:
        jugador.moveX(1)
    if  keys[pygame.K_SPACE]:
        misil = jugador.shoot()
    
        

    if misil:
        misil.moveUp()

    screen.fill(BLACK)
    screen.blit(jugador.image, jugador.getRect())
   
    if misil:
        pygame.draw.rect(screen, RED, misil.getRect())
    

    #PAUSA-----------------
    if  keys[pygame.K_p]:
        pausar()
    #----------------------
    


    pygame.display.update()

    clock.tick(60)

pygame.quit()
