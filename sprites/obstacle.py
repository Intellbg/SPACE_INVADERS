from sprites.block import Block
from pygame.sprite import Group


class Obstacle ():
    blockSize = 5
    obstacleAmount = 4
    yStart=425

    def __init__(self, screen):
        self.shape = Block.shape
        self.blocks = Group()
        offset = screen.get_width() / (self.obstacleAmount+1)
        self.obstacle_x_positions = [
            num * offset for num in range(self.obstacleAmount)]
        self.create_multiple_obstacles(
            *self.obstacle_x_positions, xStart=offset, yStart=self.yStart)

    def create_obstacle(self, xStart, yStart , offsetX):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = xStart + col_index * self.blockSize + offsetX
                    y = yStart + row_index * self.blockSize
                    block = Block(self.blockSize, (0, 255, 0), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, xStart, yStart):
        for offsetX in offset:
            self.create_obstacle(xStart, yStart, offsetX)
