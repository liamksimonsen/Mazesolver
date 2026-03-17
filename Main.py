import pygame, sys
import time
from Visuel import DrawMaze, height, width, color
from Solver import MazeSolver
from Generator import etStep, findfront, bro,tomt_board, startSlut

pygame.init()
maze = []
front = []
startX, startY = 5,5

maze = tomt_board(101,101)
maze[startY][startX] = 0
front, maze = findfront(startY,startX,maze,front)

screen = pygame.display.set_mode((width, height))

while True:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if len(front) > 0:
        front, maze = bro(front, maze)
        DrawMaze(maze,screen)
        if len(front) == 0:
            startSlut(startY,startX,maze)
    else:
        MazeSolver(maze,screen)
    pygame.display.flip()