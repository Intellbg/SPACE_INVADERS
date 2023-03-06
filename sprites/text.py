class Text():

    def __init__(self, font, text, x, y):
        self.font = font
        self.textVal = text
        self.text = font.render(text, True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (x, y)

    def checkHover(self, pos):
        if self.rect.collidepoint(pos):
            self.text = self.font.render(self.textVal, True, (0, 255, 0))
        else:
            self.text = self.font.render(self.textVal, True, (255, 255, 255))

    def getRect(self):
        return self.rect

    def getText(self):
        return self.text
    
    def display(self,screen):
        screen.blit(self.text, self.rect)
