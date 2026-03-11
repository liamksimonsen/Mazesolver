import random
import time

def tomt_board(leangde,bredde):
    board = []
    for i in range(leangde):
        board.append([])
        for k in range(bredde):
            board[i].append(1)
    return board

def findfront(x, y, board = [],front_lst = []):

    #find alle naboer og tjekker om de er en væg
    try:
        if board[y][x+2] == 1:
            board[y][x+2] = 2
            front_lst.append([y,x+2,1])
    except:
        pass
    try:
        if board[y][x-2] == 1 and x-2 > 0:
            board[y][x-2] = 2
            front_lst.append([y,x-2,2])
    except:
        pass
    try:
        if board[y+2][x] == 1:
            board[y+2][x] = 2
            front_lst.append([y+2,x,3])
    except:
        pass
    try:
        if board[y-2][x] == 1 and y-2 > 0:
            board[y-2][x] = 2
            front_lst.append([y-2,x,4])
    except:
        pass
    
    return front_lst, board

def bro(front_lst = [], board = []):
    len_front_lst = len(front_lst)
    random_tal = random.randint(0,len_front_lst-1)
    random_front = front_lst[random_tal]

    #laver en "bro" mellem en front on dens tilsvarende del af mazen
    if random_front[2] == 1:
        board[random_front[0]][random_front[1]] = 0
        board[random_front[0]][random_front[2]-1] = 0
        findfront(random_front[1]-1,random_front[0],board,front_lst)      
    elif random_front[2] == 2:
        board[random_front[0]][random_front[1]] = 0
        board[random_front[0]][random_front[1]+1] = 0
        findfront(random_front[1]+1,random_front[0],board,front_lst)
    elif random_front[2] == 3:
        board[random_front[0]][random_front[1]] = 0
        board[random_front[0]-1][random_front[1]] = 0
        findfront(random_front[1],random_front[0]-1,board,front_lst)
    elif random_front[2] == 4:
        board[random_front[0]][random_front[1]] = 0
        board[random_front[0]][random_front[1]-1] = 0
        findfront(random_front[1],random_front[0]+1,board,front_lst)
    findfront(random_front[1],random_front[0],board,front_lst)
    front_lst.pop(random_tal)
    return front_lst, board

def step(board,front_lst,y,x):
    findfront(x,y,board, front_lst)
    bro(front_lst,board)
    return front_lst, board


fronter = []
maze = tomt_board(10,10)

print(fronter, '\n', maze)

#kør programmet en gang (do while loop)
fronter, maze = findfront(0,0,maze,fronter)

print(fronter, '\n', maze)