#alle bibliotekker som skal importeres bliver importeret
import pygame, sys
from Visuel import DrawMaze, tegnStart
from Solver import MazeSolver
from Generator import etStep, findfront, bro,tomt_board, startSlut

#funktionen tegnstart kaldes som viser startskærmen derefter importeres størrelsen af skærmen
stoerrelse, instant_generer = tegnStart()
from Visuel import height, width

#sætter skærmens størrelse og starter pygame
pygame.init()
screen = pygame.display.set_mode((width, height))

#varibaler defineres
maze = []
front = []
startX, startY = 1,1

#tjekker om brugerne ville have mazen generet med det sammen
if instant_generer:
    front, maze = etStep(maze,front,stoerrelse,startX,startY)
else:
    #hvis brugerne ville have det visulet laves boardet og start postionen samt fronter findes
    maze = tomt_board(stoerrelse,stoerrelse)
    maze[startY][startX] = 0
    front, maze = findfront(startY,startX,maze,front)

#while loop som køre til at brugerne trykker kryds
running = True
while running:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #hvis mazen ikke er helt generet, genere det næste step ellers kald mazesolver
    if len(front) > 0:
        front, maze = bro(front, maze)
        DrawMaze(maze,screen)
        #finder start og slut punkter når maze er generet
        if len(front) == 0:
            startSlut(startY,startX,maze)
    else:
        MazeSolver(maze,screen)
        
    pygame.display.flip()

pygame.quit()
sys.exit()