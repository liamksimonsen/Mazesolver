import pygame, sys
import time

#vinduets dimentioner
width = 1000
height = 1000
#farverne på stien og væggen
color = [[0,0,0],[255,255,255],[255,0,0],[0,255,0],[255,255,0]]

#giver hver en box et koordinat(x og y) og farve(0 eller 1)
def MazeCordsMaker(maze, box_parameter_x, box_parameter_y):
    mazecords = []
    for y, list in enumerate(maze):
        mazecords.append([])
        for x, color in enumerate(list):
            mazecords[y].append([x*box_parameter_x,y*box_parameter_y,color])
    return(mazecords)

#Tegner hver en box
def DrawMaze(maze,screen):
    #målene på en enkelt box(væg eller sti)
    box_parameter_x = width/len(maze[1])
    box_parameter_y = height/len(maze)
    mazecords = MazeCordsMaker(maze, box_parameter_x, box_parameter_y) #Tager den generaret maze og laver den om så den kan tegnes
    for list in mazecords:
        for box_value in list:
            pygame.draw.rect(screen, color[box_value[2]], (box_value[0],box_value[1],box_parameter_x,box_parameter_y))





