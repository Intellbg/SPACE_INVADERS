from pygame import Rect, Surface
from pygame.sprite import Sprite


class Missile(Sprite):
    sizeX = 5
    sizeY = 10
    vel = -2
    missile = None
    shooted=False

    def __init__(self):
        Sprite.__init__(self)
        self.rect = Rect(-1, -100, 5, 10)
        self.image = Surface((5, 10))
        self.image.fill((0, 0, 0))

    @staticmethod
    def getInstance():
        if not Missile.missile:
            Missile.missile = Missile()
        return Missile.missile

    def setPosition(self, x, y):
        self.rect.x = x-self.sizeX/2
        self.rect.y = y-self.sizeY
        self.image.fill((0, 255, 0))
        self.shooted=True

    def update(self):
        self.rect.y += self.vel
        if self.rect.y < 0:
            self.removeFromScreen()

    def removeFromScreen(self):
        self.shooted=False
        self.rect.y = -100
        self.image.fill((0, 0, 0))

    def getY(self):
        return self.rect.y

    def getRect(self):
        return self.rect
    
    def wasShooted(self):
        return self.shooted
