import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    global x, y, r
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)

    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cursor_pos_x, cursor_pos_y = pygame.mouse.get_pos()

            if (r) >= (((( cursor_pos_x - x )**2) + ((cursor_pos_y-y)**2) )**0.5):
                print ("Cool")
            else:
                print ("Not cool")
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
