import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    resistance=3

    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def gotShoot(self):
        self.resistance-=1
        if self.resistance==2:
            self.image.fill((255,255,0))
        if self.resistance==1:
            self.image.fill((255,0,0))
        if self.resistance==0:
            self.kill()

    shape = [
        'xxxx',
        'xxxx',
    ]
