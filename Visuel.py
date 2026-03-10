import pygame, sys

import time
pygame.init()

#vinduets dimentioner
width = 500
height = 500
#farverne på stien og væggen
color = [[0,0,0],[255,255,255],[255,0,0],[0,255,0],[255,255,0]]

#målene på en enkelt box(væg eller sti)
box_parameter_x = width/len(maze[1])
box_parameter_y = height/len(maze)

#giver hver en box et koordinat(x og y) og farve(0 eller 1)
def MazeCordsMaker(maze):
    mazecords = []
    for y, list in enumerate(maze):
        mazecords.append([])
        for x, color in enumerate(list):
            mazecords[y].append([x*box_parameter_x,y*box_parameter_y,color])
    return(mazecords)

#Tegner hver en box
def DrawMaze(maze):
    mazecords = MazeCordsMaker(maze) #Tager den generaret maze og laver den om så den kan tegnes
    for list in mazecords:
        for box_value in list:
            pygame.draw.rect(screen, color[box_value[2]], (box_value[0],box_value[1],box_parameter_x,box_parameter_y))




screen = pygame.display.set_mode((width, height))
