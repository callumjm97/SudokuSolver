#!/usr/bin/env/Python3
# Author: Callum Morgan
# Date: 6th May 2020
# Description: This is a sudoku solver
import pprint
from random import randint
from time import sleep

grid = []
grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])


def checkGrid(grid):
    for row in range(2):
        for col in range(0,9):
            if grid[row][col] == 0:
                return False
    return True

def solveGrid(grid):
    for i in range(0,81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            for value in range(1,10):
                if not (value in grid[row]):
                    if not value in (grid[0][col],grid[1]):
                        grid[row][col] = value

                        if checkGrid(grid):
                            print("Grid complete and checked")
                            return True
                        else:
                            if solveGrid(grid):
                                return True
            break



pp = pprint.PrettyPrinter(width=41, compact=True)
solved = solveGrid(grid)
if solved:
    pp.pprint(grid)
    print("Sudoku completed")
else:
    print("Cannot complete this puzzle")


