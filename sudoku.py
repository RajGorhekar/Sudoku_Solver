board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# board =[
#     [4,3,5,2,6,0,7,0,1],
#     [6,8,0,0,7,0,0,9,0],
#     [1,9,0,0,0,4,5,0,0],
#     [8,2,0,1,0,0,0,4,0],
#     [0,0,4,6,2,0,9,0,0],
#     [9,5,1,7,4,3,0,2,8],
#     [0,0,9,3,0,0,0,7,4],
#     [0,4,0,0,5,0,0,3,6],
#     [7,0,3,0,1,8,2,5,9]
# ]

def printBoard(board):
    print('\n')
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(j%3==0 and j!=0):
                print '| '+str(board[i][j]),
            else:
                print board[i][j],
        if(i==2 or i==5):
            print('\n---------------------')
        else:
            print('')

def findEmpty(board):
    print('\n')
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==0):
                return(i,j)

def isValid(board,number,pos):
    for i in range(len(board[0])):
       if(board[pos[0]][i]==number and pos[1]!=i ):
           return False

    for j in range(len(board)):
       if(board[j][pos[1]]==number and pos[0]!=j ):
           return False

    cube_vertical = pos[0]//3
    cube_horizontal = pos[1]//3

    for i in range(cube_vertical*3,cube_vertical*3+3):
        for j in range(cube_horizontal*3,cube_horizontal*3+3):
            if(board[i][j]==number and (i,j)!=pos ):
                return False

    return True 
    
def solveSudoku(board):
    find = findEmpty(board)
    if not find:
        return True
    
    for i in range(1,10):
        if(isValid(board,i,find)):
            board[find[0]][find[1]]=i
            if solveSudoku(board):
                return True
            board[find[0]][find[1]]=0
    
    return False

# printBoard(board)
# a = solveSudoku(board)
# if a:
#     printBoard(board)
# else:
#     print ('unsolvable')