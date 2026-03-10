import random

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
        if board[y][x-2] == 1:
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
        if board[y-2][x] == 1:
            board[y-2][x] = 2
            front_lst.append([y-2,x,4])
    except:
        pass
    
    return front_lst, board

def bro(front_lst = [], board = []):
    len_front_lst = len(front_lst)
    random_front = front_lst[random.randint(0,len_front_lst-1)]

    #laver en "bro" mellem en front on dens tilsvarende del af mazen
    if random_front[3] == 1:
        board[random_front[1]][random_front[2]] = 0
        
    elif random_front[3] == 2:
        pass
    elif random_front[3] == 3:
        pass
    elif random_front[3] == 4:
        pass

    return front_lst, board

def step(board,front_lst):
    x = 0
    y = 0
    findfront(x,y,board, front_lst)

