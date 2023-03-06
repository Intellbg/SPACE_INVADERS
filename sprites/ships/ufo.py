from pygame.sprite import Sprite
from pygame.transform import scale
from pygame.image import load

class Ufo(Sprite):
    width = 70
    height = 70
    score = 100
    velocity = -2
    appeared=False
    image = scale(load('assets\\img\\UfoRed.png'), (width, height))
    Ufo = None

    @staticmethod
    def getInstance():
        if not Ufo.Ufo:
            Ufo.Ufo = Ufo()
        return Ufo.Ufo

    def __init__(self):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.y = 0

    def update(self):
        if self.rect.x <= 0:
            self.rect.x = -100
            self.appeared=False
        self.rect.x += self.velocity

    def setPosition(self, x):
        if self.appeared:
            return
        self.appeared=True
        self.rect.x = x

    def gotShoot(self):
        self.appeared=False
        self.rect.x = -100

    def getScore(self):
        return self.score

    def hasAppeared(self):
        return self.appeared