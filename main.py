import pygame
from screen import Screen

def main():
    pygame.init()
    screen=Screen()
    screen.displayStartScreen()
    gameover=False
    while not gameover:
        screen.playSpaceInvaders()
        gameover=screen.displayGameover()
    pygame.quit()

if __name__=="__main__":
    main()