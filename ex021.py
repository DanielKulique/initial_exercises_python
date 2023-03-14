#abrindo audio mp3


import pygame

#iniciando o Pygame
pygame.init()
#inicializando o mixer Pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021')
pygame.mixer.music.play(loops=0, start=0.0)
input()
pygame.event.wait()
