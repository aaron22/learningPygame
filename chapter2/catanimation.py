import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # main game loop
    # clear the screen
    DISPLAYSURF.fill(WHITE)
    # get the cat's new postion
    if direction == 'right':
        catx += 5
        if catx == 320:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 260:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == -20:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == -20:
            direction = 'right'
    # put that cat on the display at its new position
    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

