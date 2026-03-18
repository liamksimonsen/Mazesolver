import pygame, sys
import time

#vinduets dimentioner
width = 500
height = 500
#farverne på stien og væggen
#0 = vej, 1 = væg, 2 = sti efter gul boks, 3 = gul boks, 4 = slutning, 5 = gennemsøgt veje, 6 = farve ved søgt knudepunkt
color = [[0,0,0],[255,255,255],[0,255,0],[0,255,0],[255,255,0],[255,0,0],[255,0,0]]

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

pygame.init()

def tegnStart():
    sort = (0,0,0)
    hvid = (255,255,255)
    screen = pygame.display.set_mode((width, height))

    #font til alt tekst
    font = pygame.font.SysFont('Georgia',40,bold=True)

    #start knap
    start_knap = pygame.Rect(100,100,200,100)
    surf = font.render('Start',True, 'black')

    #bruger input
    bruger_input = ""
    text_box = pygame.Rect(300,300,100,50)
    kanSkrive = False
    farve = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_knap.collidepoint(event.pos):
                    running = False

            #bruger input
                if text_box.collidepoint(event.pos):
                    kanSkrive = True
                else:
                    kanSkrive = False
            if event.type == pygame.KEYDOWN and kanSkrive == True:
                if event.key == pygame.K_BACKSPACE:
                    bruger_input = bruger_input[:-1]
                else:
                    bruger_input += event.unicode
        
        screen.fill(sort)
        
        #tegn start knap
        pygame.draw.rect(screen,hvid,start_knap)
        screen.blit(surf,(start_knap.x+5, start_knap.y+5))

        if kanSkrive:
            farve = (255,255,255)
        else:
            farve = (255,0,0)

        #tegn bruger input
        pygame.draw.rect(screen,farve,text_box,4)
        surf_text = font.render(bruger_input,True,hvid)
        screen.blit(surf_text,(text_box.x+5,text_box.y+5))
        # ændre boks størrelse hvis tekst fylder mere, max finder den største værdi
        text_box.w = max(100,surf_text.get_width()+10)

        
        pygame.display.flip()

    return int(bruger_input)