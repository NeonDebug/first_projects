# MODULES
import pygame
from pygame.draw import *
from random import randint

pygame.init()
# VARIABLES
FPS = 1
screen = pygame.display.set_mode((1200, 900))
points = 1

# COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# FUNCTIONS THAT DRAW BALLS
def new_ball():
    global x, y, r
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)

    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def new_ball_2():
    global x2, y2, r2
    '''рисует второй шарик '''
    x2 = randint(100, 1100)
    y2 = randint(100, 900)
    r2 = randint(10, 100)

    color = COLORS[randint(0, 5)]
    circle(screen, color, (x2, y2), r2)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# EVENT

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finished = True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            cursor_pos_x, cursor_pos_y = pygame.mouse.get_pos()

            if r >= ((((cursor_pos_x - x ) ** 2) + ((cursor_pos_y - y) ** 2)) ** 0.5):
                if r < 20:
                    print(points)
                    points =+ 5
                if r > 20:
                    print(points)
                    points =+ 1

            else:
                print("Missed")

    # USING FUCTIONS

    new_ball()
    new_ball_2()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
