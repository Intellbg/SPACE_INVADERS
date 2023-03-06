import pygame
from escenario import Escenario

pygame.mixer.music.load('sounds/sound.mp3')
pygame.mixer.music.play()
juego = Escenario()
juego.iniciarPrograma()

