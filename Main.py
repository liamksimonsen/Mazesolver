import pygame, sys
import time
from Visuel import DrawMaze, height, width, color
from Solver import MazeSolver
from Generator import etStep

pygame.init()
maze = []
front = []
front, maze = etStep(maze,front,100,100)

screen = pygame.display.set_mode((width, height))

while True:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    MazeSolver(maze,screen)
    pygame.display.flip()

