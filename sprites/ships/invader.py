import pygame
from pygame.sprite import Sprite
from pygame.transform import scale
from pygame.image import load


def change_image_on_event(screen, event, old_image_path, new_image_path):

    # Load the old and new images
    old_image = pygame.image.load(old_image_path)
    new_image = pygame.image.load(new_image_path)

    # Check for the specified Pygame event
    if event.type == pygame.KEYDOWN:
        # Replace the old image with the new image
        screen.blit(new_image, (0, 0))
        # Update the display
        pygame.display.update()
    else:
        # Display the old image
        screen.blit(old_image, (0, 0))
        # Update the display
        pygame.display.update()


class Invader(Sprite):
    width = 50
    height = 50
    velocity = 1
    currentImg=0
    direction=1

    def __init__(self, i, j, screen, imgPath=['assets\img\Crab1.png','assets\img\Crab2.png'],):
        super().__init__()
        self.images=[
            scale(load(imgPath[0]), (self.width, self.height)),
            scale(load(imgPath[1]), (self.width, self.height))
        ]
        self.image = self.images[0]
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = i * (self.width-10)
        self.rect.y = j * (self.height-10) + self.height
        self.X_MAX = screen.get_width()

    def moveNave(self):
        if (position > 0):
            position -= self.velocity
        else:
            if (position < self.X_MAX):
                position += self.velocity

    def update(self,screenCollision=False):
        if screenCollision:
            self.direction*=-1
            self.rect.y+=self.height
        self.currentImg+=0.05
        if self.currentImg >= len(self.images):
            self.currentImg=0
            self.image=self.images[0]

        self.image=self.images[int(self.currentImg)] 
        self.rect.x+=self.velocity*self.direction


        


class Squid(Invader):
    def __init__(self, i, j, screen):
        super().__init__(i, j, screen, ['assets\img\Squid1.png','assets\img\Squid2.png'])


class Octopus(Invader):
    def __init__(self, i, j, screen):
        super().__init__(i, j, screen, ['assets\img\Octopus1.png','assets\img\Octopus2.png'])
