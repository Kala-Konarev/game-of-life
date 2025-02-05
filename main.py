import pygame
from random import randint
from copy import deepcopy

W = 1000
H = 500
alive = (160, 200, 120)
dead = (39, 102, 123)
background = (20, 61, 96)
cellSize = 10
initialAlive = 500
ALIVE = 1
DEAD = 0
OTHER = -1

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),  # Top-left, Top, Top-right
    (0, -1),
    (0, 1),  # Left,        Right
    (1, -1),
    (1, 0),
    (1, 1),
]  # Bottom-left, Bottom, Bottom-right


rows = int(W / cellSize)
cols = int(H / cellSize)
cells = [[0 for _ in range(cols)] for _ in range(rows)]


def main():
    states = [[DEAD for _ in range(cols)] for _ in range(rows)]

    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    running = True

    populateRandomCells(initialAlive, states)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_c]:
                running = False
            if pygame.key.get_pressed()[pygame.K_r]:
                populateRandomCells(initialAlive, states)

        states = updateStates(states)
        screen.fill(background)
        drawGrid(states)
        pygame.display.flip()

        clock.tick(15)

    pygame.quit()


def getState(r, c, st, states):
    nbrsAlive = sum(
        1
        for dr, dc in directions
        if 0 <= r + dr < rows and 0 <= c + dc < cols and states[r + dr][c + dc] == ALIVE
    )

    if nbrsAlive < 2 or nbrsAlive > 3:
        return DEAD
    if nbrsAlive == 3:
        return ALIVE
    if nbrsAlive == 2:
        return st == ALIVE


def updateStates(states):
    newStates = deepcopy(states)
    for x in range(rows):
        for y in range(cols):
            newState = getState(x, y, states[x][y], states)
            newStates[x][y] = newState
    return newStates


def drawGrid(states):
    for x in range(rows):
        for y in range(cols):
            rect = pygame.Rect(x * cellSize, y * cellSize, cellSize, cellSize)
            cells[x][y] = rect
            [fill, color] = [0, alive] if states[x][y] == ALIVE else [1, dead]
            pygame.draw.rect(screen, color, rect, fill)


def populateRandomCells(amount, states):
    for _ in range(amount):
        states[randint(0, rows - 1)][randint(0, cols - 1)] = ALIVE


main()
