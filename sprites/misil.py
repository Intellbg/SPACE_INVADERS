from pygame.sprite import Sprite

class Misil(Sprite):
    x = 0
    y = 0
    size = 10
    vel = -2
    misil=None

    def __init__(self,xi,yi):
        Sprite.__init__(self)
        self.x=xi-self.size/2
        self.y=yi-self.size

    def setPosition(self,x,y):
        self.x=x-self.size/2
        self.y=y-self.size


    def moveUp(self):
        self.y+=self.vel
        if self.y<0:
            self.y=-1

    def getY(self):
        return self.y

    def getRect(self):
        return (self.x, self.y, self.size, self.size)