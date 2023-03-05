from pygame import Rect
from pygame.sprite import Sprite

class Missile(Sprite):
    GREEN=(0, 255, 0)
    BLACK=(0,0, 0)
    x = 0
    y = 0
    size = 10
    vel = -2
    missile=None
    color=GREEN

    def __init__(self):
        Sprite.__init__(self)
        self.rect = Rect(-1,0,5,10)
    
    @staticmethod
    def getInstance():
        if not Missile.missile:
            Missile.missile=Missile()
        return Missile.missile

    def setPosition(self,x,y):
        self.rect.x=x-self.size/2
        self.rect.y=y-self.size
        self.color=self.GREEN

    def update(self):
        self.rect.y+=self.vel
        if self.rect.y<0:
            self.removeFromScreen()

    def removeFromScreen(self):
        self.rect.y=-1
        self.color=self.BLACK
    
    def getY(self):
        return self.rect.y

    def getRect(self):
        return self.rect