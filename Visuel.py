import pygame

pygame.init()
#vinduets dimentioner
info = pygame.display.Info()
width = 500
height = 500
#farverne på stien og væggen
#0 = vej, 1 = væg, 2 = sti efter gul boks, 3 = gul boks, 4 = slutning, 5 = gennemsøgt veje
color = [[255,255,255],[0,0,0],[0,255,0],[0,255,0],[255,255,0],[173,173,173]]

#finder størrelsen af skræmen
def findStoerrelse(mazestr):
    #specificere af det er de global variabler som skal ændres
    global width
    global height
    #loop der tjekker hvilken størrelse af skræmen som går op i størrelsen af mazen
    for i in range(500,700,1):
        if i/mazestr % 1 == 0:
            width, height = i, i
            print(1,width)
            break
            
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
    box_parameter_x = int(width/len(maze[1]))
    box_parameter_y = int(height/len(maze))
    mazecords = MazeCordsMaker(maze, box_parameter_x, box_parameter_y) #Tager den generaret maze og laver den om så den kan tegnes
    for liste in mazecords:
        for box_value in liste:
            pygame.draw.rect(screen, color[box_value[2]], (box_value[0],box_value[1],box_parameter_x,box_parameter_y))

def tegnStart():
    sort = (0,0,0)
    hvid = (255,255,255)
    grøn = (0,255,0)
    screen = pygame.display.set_mode((500, 500))

    #fonter til tekst
    font_stor = pygame.font.SysFont('consolas',60,bold=True)
    font_lille = pygame.font.SysFont('consolas',20)

    #start knap
    start_knap = pygame.Rect(100,100,200,100)
    surf_start = font_stor.render('Start',True, 'black')

    #bruger input
    surf_brugerinput = font_lille.render('Indsæt størrelsen af mazen',True, 'white')
    bruger_input = ""
    text_box = pygame.Rect(100,230,100,70)
    kanSkrive = False
    farve = 0

    #"generer maze med det sammen" knap
    generer_knap = pygame.Rect(100,350,50,50)
    surf_generer = font_lille.render('Generer Maze med det samme',True, 'white')
    color_generer = hvid
    instant_generer = False


    #while loop som kører indtil brugerne har trykket på start
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #tjekker om bruger har trykket start
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
            
            #tjekker om bruger gerne ville have mazen generet med det sammen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if generer_knap.collidepoint(event.pos):
                    instant_generer = True
                    color_generer = grøn

        
        screen.fill(sort)
        
        #tegn start knap
        pygame.draw.rect(screen,hvid,start_knap)
        screen.blit(surf_start,(start_knap.x+5, start_knap.y+20))

        if kanSkrive:
            farve = (255,255,255)
        else:
            farve = (255,0,0)

        #tegn bruger input
        pygame.draw.rect(screen,farve,text_box,4)
        surf_text = font_stor.render(bruger_input,True,hvid)
        screen.blit(surf_text,(text_box.x+5,text_box.y+5))
        # ændre boks størrelse hvis tekst fylder mere, max finder den største værdi
        text_box.w = max(100,surf_text.get_width()+10)

        screen.blit(surf_brugerinput,(text_box.x,text_box.y-25))

        #tegn generer knap
        pygame.draw.rect(screen,color_generer,generer_knap)
        screen.blit(surf_generer,(generer_knap.x,generer_knap.y-25))

        #tester om brugeren har inputet noget andet end et tal og sletter det
        try:
            bruger_input = str(int(float(bruger_input)))
        except:
            bruger_input = bruger_input[:-1]

        pygame.display.flip()
    

    #sikre at mazen er en ullige størrelse 
    bruger_input = int(float(bruger_input))
    if bruger_input%2 == 0:
        bruger_input +=1
    
    findStoerrelse(bruger_input)
    
    return bruger_input, instant_generer