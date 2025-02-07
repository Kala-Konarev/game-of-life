from math import floor
import pygame

from grid import Grid

W = 1000
H = 600
cellSize = 25
initialAlive = 200


def main():
    # initialize loop and grid
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    running = True
    paused = False
    grid = Grid(W, H, cellSize, screen)

    # spawn initial alive cells
    grid.populateRandomCells(initialAlive)
    grid.draw()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_x
            ):
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                grid.populateRandomCells(initialAlive)
                grid.draw()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = not paused
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                grid.clear()
                grid.draw()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                x = mousePos[0] // cellSize
                y = mousePos[1] // cellSize
                grid.setCellAlive(x, y)
                grid.draw()
        if not paused:
            grid.update()
            clock.tick(15)
        pygame.display.flip()

    pygame.quit()


main()
