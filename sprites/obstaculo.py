import pygame

from bloque_proteccion import Block

class Obstacle ():
    def __init__(self):
            self.shape = bloque_proteccion.shape
            self.block_size = 6
            self.blocks = pygame.sprite.Group()
            self.obstacle_amount = 4
            self.obstacle_x_positions = [
                num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
            self.create_multiple_obstacles(
                *self.obstacle_x_positions, x_start=screen_width / 15, y_start=480)

    def create_obstacle(self, x_start, y_start, offset_x):
                for row_index, row in enumerate(self.shape):
                    for col_index, col in enumerate(row):
                        if col == 'x':
                            x = x_start + col_index * self.block_size + offset_x
                            y = y_start + row_index * self.block_size
                            block = bloque_proteccion.Block(
                                self.block_size, (241, 79, 80), x, y)
                            self.blocks.add(block)

    def create_multiple_obstacles(self,*offset,x_start,y_start):
    		for offset_x in offset:
    			self.create_obstacle(x_start,y_start,offset_x)
