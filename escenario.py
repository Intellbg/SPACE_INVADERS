import pygame
from pygame.sprite import Group, spritecollideany
from sprites.block import Block
from sprites.missile import Missile
from sprites.obstacle import Obstacle
from sprites.ships.invader import Octopus, Squid, Invader
from sprites.ships.defense import NaveDefensora
pygame.init() 

RED = (255, 0, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 563

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# PANTALLA DE PAUSA------------------------------------------------------------------------
font = pygame.font.Font(None, 70)

text_surfacePausa = font.render("PAUSA", True, (255, 0, 128))
text_pausa = text_surfacePausa.get_rect()
text_pausa.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

text_surfaceR = font.render(
    "Presiona la tecla R para continuar", True, (255, 177, 187))
text_R = text_surfaceR.get_rect()
text_R.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
# ----------------------------------------------------------------------------------------


# CONFIGURACION PESTAÑA----------------------------------------------------
pygame.display.set_caption("SPACE INVADERS")
icono = pygame.image.load('assets/img/UfoRed.png').convert_alpha()
pygame.display.set_icon(icono)
# ------------------------------------------------------


running = True
final = True

clock = pygame.time.Clock()
velocidadNave = 0
player = NaveDefensora(SCREEN_WIDTH, SCREEN_HEIGHT)
missile = Missile.getInstance()

aliens = Group()
for i in range(12):
    for j in range(5):
        if j == 0:
            aliens.add(Squid(i, j, screen))
        elif j > 2:
            aliens.add(Octopus(i, j, screen))
        else:
            aliens.add(Invader(i, j, screen))

obstacle=Obstacle(screen)

all_sprites = Group()
all_sprites.add(aliens)
all_sprites.add(player)
# Funcion pausar()

missileCollisionable = Group()
missileCollisionable.add(aliens)
missileCollisionable.add(obstacle.blocks)

def pausar():
    global running
    pausa = True
    while pausa:
        # Imprimir mensaje en pantalla------------
        screen.blit(text_surfacePausa, text_pausa)
        screen.blit(text_surfaceR, text_R)
        pygame.display.update()
        # ----------------------------------------

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveX(-1)
    if keys[pygame.K_RIGHT]:
        player.moveX(1)
    if keys[pygame.K_SPACE]:
        player.shoot()
    if keys[pygame.K_p]:
        pausar()

    screen.fill(BLACK)
    all_sprites.update()

    # Handle aliens of screen
    for alien in aliens:
        if not screen.get_rect().contains(alien):
            aliens.update(screenCollision=True)
            break

    # Missile alien
    missileCollision = spritecollideany(missile, missileCollisionable)
    if missileCollision:
        if isinstance(missileCollision,Block):
            missileCollision.gotShoot()
        if isinstance(missileCollision,Invader):            
            missileCollision.kill()
            missile.removeFromScreen()

    
    missile.update()
    pygame.draw.rect(screen, missile.color, missile.getRect())

    
    for block in obstacle.blocks:
        screen.blit(block.image, block.rect)


    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
