import pygame, sys
from Visuel import DrawMaze, height, width, color
import time
import random
pygame.init()


def FindStartPosition(maze):
    for y, list in enumerate(maze):
        for x, color in enumerate(list):
            if color == 4:
                return [x,y] 
            
def FindVeje(maze, position):
    muligeveje = []
    if maze[position[1]-1][position[0]] == 0:
        muligeveje.append([position[0],position[1]-1])
    if maze[position[1]+1][position[0]] == 0:
        muligeveje.append([position[0],position[1]+1])
    if maze[position[1]][position[0]+1] == 0:
        muligeveje.append([position[0]+1,position[1]])
    if maze[position[1]][position[0]-1] == 0:
        muligeveje.append([position[0]-1,position[1]])
    return muligeveje

def Move(maze, position, endeposition):
    maze[endeposition[1]][endeposition[0]] = 4
    maze[position[1]][position[0]] = 2
    return maze


def MazeSolver(maze, screen):
    knudepunkt = []
    DrawMaze(maze, screen)
    while True:
        time.sleep(0.2)
        position = FindStartPosition(maze)
        Veje = FindVeje(maze,position)
        if len(Veje) == 1:
            maze = Move(maze, position, Veje[0])
            DrawMaze(maze, screen)
        if len(Veje) > 1:
            knudepunkt.append(position)
            maze = Move(maze, position, Veje[random.randint(0,len(Veje)-1)])
            DrawMaze(maze, screen)
        if len(Veje) == 0:
            while True:
                Veje = FindVeje(maze,knudepunkt[-1])
                if len(Veje) == 0:
                    knudepunkt.pop()
                else:
                    break
            maze = Move(maze, knudepunkt[-1], Veje[random.randint(0,len(Veje)-1)])
        pygame.display.flip()
        print(knudepunkt)
    print('Stoppet')
