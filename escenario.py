import pygame
from sprites.misil import Misil

from sprites.naves.nave_defensora import NaveDefensora

#from sprites.bloque_proteccion import Block


pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 563

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



pygame.display.set_caption("SPACE INVADERS")

running = True

clock = pygame.time.Clock()

class Obstacle:
    def __init__(self):
            self.shape = bloque_proteccion.shape
            self.block_size = 6
            self.blocks = pygame.sprite.Group()
            self.obstacle_amount = 4
            self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
            self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = screen_width / 15, y_start = 480)
    
    def create_obstacle(self, x_start, y_start,offset_x):
                for row_index, row in enumerate(self.shape):
                    for col_index,col in enumerate(row):
                        if col == 'x':
                            x = x_start + col_index * self.block_size + offset_x
                            y = y_start + row_index * self.block_size
                            block = bloque_proteccion.Block(self.block_size,(241,79,80),x,y)
                            self.blocks.add(block)



jugador = NaveDefensora(SCREEN_WIDTH,SCREEN_HEIGHT)
velocidadNave = 0
misil = None
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
    pygame.display.update()

    
    clock.tick(60)
pygame.quit()
