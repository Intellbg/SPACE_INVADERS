from pygame import Rect, Surface
from pygame.sprite import Sprite

class Lasser(Sprite):
    size = 10
    vel = 2
    lasser = None
    shooted=False

    def __init__(self):
        Sprite.__init__(self)
        self.rect = Rect(0, -3, 5, 10)
        self.image = Surface((5, 10))
        self.image.fill((0, 0, 0))

    @staticmethod
    def getInstance():
        if not Lasser.lasser:
            Lasser.lasser = Lasser()
        return Lasser.lasser

    def setPosition(self, x, y):
        self.rect.x = x-self.size/2
        self.rect.y = y-self.size
        self.image.fill((255, 255, 255))
        self.shooted=True

    def update(self):
        if self.shooted:
            self.rect.y += self.vel
            if self.rect.y > 563:
                self.removeFromScreen()

    def removeFromScreen(self):
        self.shooted=False
        self.image.fill((0, 0, 0))

    def getY(self):
        return self.rect.y

    def getRect(self):
        return self.rect
