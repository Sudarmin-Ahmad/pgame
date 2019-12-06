# Pemrograman Game Praktikum 7
# latihan code 7.1 : PyGame

import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((700, 500))

pygame.display.set_caption('MY NAME IS : SUDARMIN A. AHMAD')

while True: # main game loop
	for event in pygame.event.get();
	if event.type == QUIT:
		pygame.quit()
	pygame.display.update()