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
    print("fronter findes...", y, x)
    #find alle naboer og tjekker om de er en væg
    try:
        if board[y][x+2] == 1 and board[y][x+1] != 2 and board[y][x-1] != 2 and board[y+1][x] != 2 and board[y-1][x] != 2:
            board[y][x+2] = 2
            front_lst.append([y,x+2,y,x+1])
            #print(y,x+2)
    except:
        pass
    try: #behøver ikke at være i en try
        if board[y][x-2] == 1 and x-2 > 0 and board[y][x+1] != 2 and board[y][x-1] != 2 and board[y+1][x] != 2 and board[y-1][x] != 2:
            board[y][x-2] = 2
            front_lst.append([y,x-2,y,x-1])
            #print(y,x-2)
    except:
        pass
    try:
        if board[y+2][x] == 1 and board[y][x+1] != 2 and board[y][x-1] != 2 and board[y+1][x] != 2 and board[y-1][x] != 2:
            board[y+2][x] = 2
            front_lst.append([y+2,x,y+1,x])
            #print(y+2,x)
    except:
        pass
    try: #behøver ikke at være i en try
        if board[y-2][x] == 1 and y-2 > 0 and board[y][x+1] != 2 and board[y][x-1] != 2 and board[y+1][x] != 2 and board[y-1][x] != 2:
            board[y-2][x] = 2
            front_lst.append([y-2,x,y-1,x])
            #print(y-2,x)
    except:
        pass
    
    return front_lst, board

def bro(front_lst = [], board = []):
    len_front_lst = len(front_lst)
    random_tal = random.randint(0,len_front_lst-1)
    random_front = front_lst[random_tal]

    findfront(random_front[0],random_front[1],board,front_lst)
    findfront(random_front[2],random_front[3],board,front_lst)

    #laver en "bro" mellem en front on dens tilsvarende del af mazen
    board[random_front[0]][random_front[1]] = 0
    board[random_front[2]][random_front[3]] = 0

    front_lst.pop(random_tal)
    return front_lst, board

def etStep(board,front_lst,strY,strX,y = 5,x = 5):
    board = tomt_board(strY,strX)

    findfront(y,x,board, front_lst)

    while len(front_lst) > 0:
        bro(front_lst,board)
    
    board[y][x] = 4
    for i in range(strX):
        if board[strY-1][strX-i] == 0:
            board[strY-1][strX-i] = 3
            break

    return front_lst, board


fronter = []
maze = []

fronter, maze = etStep(maze, fronter, 30, 30)

print(maze)

"""
fronter, maze = findfront(10,10,maze,fronter)
print(maze,'\n', "-------------------------------")
#fronter, maze = bro(fronter, maze)
for k in range(1000):
    print(maze)
    fronter, maze = bro(fronter, maze)
    for i in range(len(maze)):
        print(maze[i])
    print("---------------------------------")
print(maze)
"""
