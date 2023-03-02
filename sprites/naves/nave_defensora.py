from pygame.sprite import Sprite
from pygame.transform import scale
from pygame.image import load

from sprites.misil import Misil


class NaveDefensora(Sprite):
    width = 70
    height = 70
    image = scale(load('assets\img\LaserCannon.png'), (width, height))
    nave = image.get_rect()
    velocity = 4
    misil=None

    def __init__(self, screen_width, screen_height):
        Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height - 100
        self.X_MAX=screen_width

    def shoot(self):
        if not self.misil:
            self.misil=Misil(self.getX() + self.width/2, self.getY())
        if self.misil.getY()==-1:
            self.misil.setPosition(self.getX() + self.width/2, self.getY())
        return self.misil 


    def moveX(self, dx):
        self.rect.x += dx*self.velocity
        if self.getX() < 0:
            print("CHOQUE IZ")
            self.rect.x=0
        if self.getX() + self.width > self.X_MAX:
            print("CHOQUE DER")
            self.rect.x=self.X_MAX - self.width

    def getRect(self):
        return self.rect

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

