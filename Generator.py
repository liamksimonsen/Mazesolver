import random
import time

def tomt_board(leangde,bredde):
    board = []
    for i in range(leangde):
        board.append([])
        for k in range(bredde):
            board[i].append(1)
    return board

def findfront(y,x, board = [],front_lst = []): #skal kunne tjekke om det stadig er en front

    #find alle naboer og tjekker om de er en væg
    if y - 2 >= 0:
        if board[y][x] != 2:
            if x + 2 < len(board[0]) - 1:
                if board[y][x+2] == 1:
                    board[y][x+2] = 2
                    front_lst.append([y,x+2])
            if board[y][x-2] == 1 and x-2 > 0:
                board[y][x-2] = 2
                front_lst.append([y,x-2])
            if y + 2 < len(board) - 1:
                if board[y+2][x] == 1:
                    board[y+2][x] = 2
                    front_lst.append([y+2,x])
            if board[y-2][x] == 1 and y-2 > 0:
                board[y-2][x] = 2
                front_lst.append([y-2,x])
    
    return front_lst, board

def bro(front_lst = [], board = []):
    # finder en tilfældig front
    len_front_lst = len(front_lst)
    random_tal = random.randint(0,len_front_lst-1)
    random_front = front_lst[random_tal]

    # finder alle naboer som er en vej i mazen til den tilfældige front
    naboVej = []
    if random_front[0]+2 < len(board)-1 and board[random_front[0]+2][random_front[1]] == 0:
        naboVej.append([random_front[0]+1, random_front[1]])

    if random_front[0]-2 >= 0 and board[random_front[0]-2][random_front[1]] == 0:
        naboVej.append([random_front[0]-1, random_front[1]])

    if random_front[1]+2 < len(board[0])-1 and board[random_front[0]][random_front[1]+2] == 0:
        naboVej.append([random_front[0], random_front[1]+1])

    if random_front[1]+2 >= 0 and board[random_front[0]][random_front[1]-2] == 0:
        naboVej.append([random_front[0], random_front[1]-1])
    
    #finder en en tilfældig nabo
    random_nabo = naboVej[random.randint(0,len(naboVej)-1)]
    
    board[random_front[0]][random_front[1]] = 0
    board[random_nabo[0]][random_nabo[1]] = 0

    findfront(random_front[0],random_front[1],board,front_lst)
    front_lst.pop(random_tal)
    return front_lst, board

def etStep(board,front_lst,strY,strX,y = 5,x = 5):
    board = tomt_board(strY,strX)
    board[y][x] = 0

    findfront(y,x,board, front_lst)

    while len(front_lst) > 0:
        bro(front_lst,board)
    
    board[y][x] = 4
    for i in range(strX):
        if board[strY-1][strX-i-1] == 0:
            board[strY-1][strX-i-1] = 3
            break

    return front_lst, board

def startSlut(y,x,board):
    board[y][x] = 4
    for i in range(len(board[1])):
        if board[len(board)-2][len(board[1])-i-1] == 0:
            board[len(board)-2][len(board[1])-i-1] = 3
            break
