import pygame

pygame.init()

RED = (255, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 563

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('espacio.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("SPACE INVADERS")

#BALA
bala_x = 0
bala_y = 0
bala_size = 10
bala_vel = -2

running = True

def cerrarJuego(running):
    running = False
    return running 

width = 70
height = 70
image = pygame.transform.scale(pygame.image.load('nave.png'), (width, height))

nave = image.get_rect()

velocidadNave = 0

nave.y = SCREEN_HEIGHT - 100


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrarJuego()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                cerrarJuego()
            if event.key == pygame.K_LEFT:
                velocidadNave = -1
            elif event.key == pygame.K_RIGHT:
                velocidadNave = 1
            elif event.key == pygame.K_SPACE:
                bala_x = nave.x + 70/2 - bala_size/2
                bala_y = nave.y - bala_size
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                velocidadNave = 0


    
    nave.x += velocidadNave

    # Make sure the square stays within the screen
    if nave.x < 0:
        nave.x = 0
    elif nave.x + 70 > SCREEN_WIDTH:
        nave.x = SCREEN_WIDTH - 70

    # Update the position of the bala based on its velocity
    bala_y += bala_vel

    # Check if the bala has gone off the top of the screen
    if bala_y < 0:
        bala_y = 0

    screen.blit(background, (0, 0))
    screen.blit(image, nave)
    pygame.draw.rect(screen, RED, (bala_x, bala_y, bala_size, bala_size))

    pygame.display.update()

pygame.quit()