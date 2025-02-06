from copy import deepcopy
import pygame
from random import randint

from cell import Cell
from colors import *
from states import *

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


class Grid:
    def __init__(self, w, h, cellSize, screen):
        self.rows = int(w / cellSize)
        self.cols = int(h / cellSize)
        self.cellSize = cellSize
        self.cells = [[Cell(x, y) for y in range(self.cols)] for x in range(self.rows)]
        self.screen = screen

    def getNextState(self, x, y):
        # Get number of living neighbors
        nbrsAlive = sum(
            1
            for dr, dc in directions
            if 0 <= x + dr < self.rows
            and 0 <= y + dc < self.cols
            and self.cells[x + dr][y + dc].state == ALIVE
        )
        state = self.cells[x][y].state

        # Determine next state based on number of living neighbors
        if nbrsAlive < 2 or nbrsAlive > 3:
            return DEAD
        if nbrsAlive == 3:
            return ALIVE
        if nbrsAlive == 2:
            return state == ALIVE

    def update(self):
        # Save the state of the grid to simulate simultanious cell updates
        newStates = deepcopy(self.cells)
        for x in range(self.rows):
            for y in range(self.cols):
                # For each cell update the state individually
                newStates[x][y].state = self.getNextState(x, y)
        # Update the cell matrix and rerender
        self.cells = newStates
        self.draw()

    def draw(self):
        self.screen.fill(colBackground)
        for x in range(self.rows):
            for y in range(self.cols):
                # Create cell
                rect = pygame.Rect(
                    x * self.cellSize, y * self.cellSize, self.cellSize, self.cellSize
                )
                # Determine color
                [fill, color] = (
                    [0, colAlive] if self.cells[x][y].state == ALIVE else [1, colDead]
                )
                # Draw cell
                pygame.draw.rect(self.screen, color, rect, fill)

    def populateRandomCells(self, amount):
        for _ in range(amount):
            self.cells[randint(0, self.rows - 1)][
                randint(0, self.cols - 1)
            ].state = ALIVE
