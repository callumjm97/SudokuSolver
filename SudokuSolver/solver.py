#!/usr/bin/env/Python3
# Author: Callum Morgan
# Date: 6th May 2020
# Description: This is a sudoku solver
import pprint
from random import randint
from time import sleep
from datetime import datetime

startTime = datetime.now()

grid = []
grid.append([6, 9, 0, 0, 0, 0, 0, 0, 7])
grid.append([4, 0, 0, 9, 3, 0, 6, 0, 0])
grid.append([5, 0, 2, 0, 0, 7, 0, 1, 0])
grid.append([0, 0, 9, 0, 0, 0, 2, 0, 1])
grid.append([0, 1, 0, 0, 7, 0, 0, 8, 0])
grid.append([8, 0, 0, 0, 0, 0, 7, 0, 0])
grid.append([0, 5, 0, 8, 0, 0, 0, 0, 6])
grid.append([0, 0, 3, 0, 2, 4, 0, 0, 8])
grid.append([9, 0, 0, 0, 0, 0, 0, 5, 2])

def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                return False
    return True

def solveGrid(grid):
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:
                square=[grid[i][6:9] for i in range(6,9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if checkGrid(grid):
                print("Grid Complete and Checked")
                return True
              else:
                if solveGrid(grid):
                  return True
      break
  print("Backtrack")
  grid[row][col]=0


pp = pprint.PrettyPrinter(width=41, compact=True)
solved = solveGrid(grid)
if solved:
    pp.pprint(grid)
    print("Sudoku completed")
else:
    print("Cannot complete this puzzle")

print("runtime: ", datetime.now() - startTime)

