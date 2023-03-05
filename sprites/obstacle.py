import pygame
from sprites.block import Block
from pygame.sprite import Group


class Obstacle ():
    blockSize = 5
    obstacleAmount = 4

    def __init__(self, screen):
        self.shape = Block.shape
        self.blocks = Group()
        offset = screen.get_width() / (self.obstacleAmount+1)
        self.obstacle_x_positions = [
            num * offset for num in range(self.obstacleAmount)]
        self.create_multiple_obstacles(
            *self.obstacle_x_positions, x_start=offset, y_start=400)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.blockSize + offset_x
                    y = y_start + row_index * self.blockSize
                    block = Block(
                        self.blockSize, (0, 255, 0), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)
