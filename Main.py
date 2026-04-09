import pygame, sys
from Visuel import DrawMaze, tegnStart, height, width
from Solver import MazeSolver
from Generator import etStep, findfront, bro,tomt_board, startSlut


pygame.init()
screen = pygame.display.set_mode((width, height))

stoerrelse, instant_generer = tegnStart()

maze = []
front = []
startX, startY = 1,1

if instant_generer:
    front, maze = etStep(maze,front,stoerrelse,startX,startY)
else:
    maze = tomt_board(stoerrelse,stoerrelse)
    maze[startY][startX] = 0
    front, maze = findfront(startY,startX,maze,front)

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