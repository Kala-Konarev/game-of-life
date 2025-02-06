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
                event.type == pygame.KEYDOWN and event.key == pygame.K_c
            ):
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                grid.populateRandomCells(initialAlive)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = not paused
        if not paused:
            grid.update()
            clock.tick(15)
        pygame.display.flip()

    pygame.quit()


main()
