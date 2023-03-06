from pygame.sprite import Sprite
from pygame.transform import scale
from pygame.image import load
from sprites.lasser import Lasser


class Invader(Sprite):
    width = 50
    height = 50
    velocity = 1
    currentImg = 0
    direction = 1
    score = 20

    def __init__(self, i, j, screen, imgPath=['assets\img\Crab1.png', 'assets\img\Crab2.png'],):
        super().__init__()
        self.images = [
            scale(load(imgPath[0]), (self.width, self.height)),
            scale(load(imgPath[1]), (self.width, self.height))
        ]
        self.image = self.images[0]
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = i * (self.width-10)
        self.rect.y = j * (self.height-10) + self.height
        self.X_MAX = screen.get_width()

    def update(self, screenCollision=False):
        if screenCollision:
            self.direction *= -1
            self.rect.y += self.height/2
        self.currentImg += 0.05
        if self.currentImg >= len(self.images):
            self.currentImg = 0
            self.image = self.images[0]

        self.image = self.images[int(self.currentImg)]
        self.rect.x += self.velocity*self.direction

    def shoot(self):
        lasser = Lasser.getInstance()
        if lasser.shooted == False:
            lasser.setPosition(self.rect.x + self.width/2, self.rect.y)

    def getScore(self):
        return self.score
    
    def getY(self):
        return self.rect.y

class Squid(Invader):
    score = 30

    def __init__(self, i, j, screen):
        super().__init__(i, j, screen, [
            'assets\img\Squid1.png', 'assets\img\Squid2.png'])


class Octopus(Invader):
    score = 10

    def __init__(self, i, j, screen):
        super().__init__(i, j, screen, [
            'assets\img\Octopus1.png', 'assets\img\Octopus2.png'])


