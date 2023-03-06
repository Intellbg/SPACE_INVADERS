from pygame.sprite import Sprite
from pygame.transform import scale
from pygame.image import load

from sprites.missile import Missile


class Defender(Sprite):
    width = 70
    height = 70
    image = scale(load('assets\img\LaserCannon.png'), (width, height))
    nave = image.get_rect()
    velocity = 4
    life=3

    def __init__(self, screen_width, screen_height):
        Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height - 100
        self.X_MAX=screen_width

    def shoot(self):
        missile=Missile.getInstance()
        if not missile.wasShooted():
            missile.setPosition(self.getX() + self.width/2, self.getY())

    def gotShoot(self):
        self.life-=1
        return self.life!=0

    def moveX(self, dx):
        self.rect.x += dx*self.velocity
        if self.getX() < 0:
            self.rect.x=0
        if self.getX() + self.width > self.X_MAX:
            self.rect.x=self.X_MAX - self.width

    def getLife(self):
        return self.life

    def getRect(self):
        return self.rect

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

