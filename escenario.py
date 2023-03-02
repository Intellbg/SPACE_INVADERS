import pygame
from sprites.misil import Misil

from sprites.naves.nave_defensora import NaveDefensora

pygame.init()

RED = (255, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 563

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('assets\img\espacio.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("SPACE INVADERS")

running = True


def cerrarJuego():
    return False
clock = pygame.time.Clock()

jugador = NaveDefensora(SCREEN_WIDTH,SCREEN_HEIGHT)
velocidadNave = 0
misil = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrarJuego()
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

    screen.blit(background, (0, 0))
    screen.blit(jugador.image, jugador.getRect())
    if misil:
        pygame.draw.rect(screen, RED, misil.getRect())
    pygame.display.update()
    clock.tick(60)
pygame.quit()
