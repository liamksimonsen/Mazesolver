import random

def findfront(x, y, board = [],front_lst = []):

    #find alle naboer og tjekker om de er en væg
    try:
        if board[y][x+2] == 1:
            board[y][x+2] = 2
            front_lst.append([y,x+2])
    except:
        pass
    try:
        if board[y][x-2] == 1:
            board[y][x-2] = 2
            front_lst.append([y,x-2])
    except:
        pass
    try:
        if board[y+2][x] == 1:
            board[y+2][x] = 2
            front_lst.append([y+2,x])
    except:
        pass
    try:
        if board[y-2][x] == 1:
            board[y-2][x] = 2
            front_lst.append([y-2,x])
    except:
        pass
    
    return front_lst

def bro(front_lst = [], board = []):
    len_front_lst = len(front_lst)
    random_front = front_lst[random.randint(0,len_front_lst-1)]
    
    return front_lst, board
