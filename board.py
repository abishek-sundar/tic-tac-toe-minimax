import random
def printBoard(board):
    for row in board:
        print ('{l[0]} {l[1]} {l[2]}'.format(l=row))
    print()

def resetBoard():
    board = [['-' for i in range(3)] for j in range(3)]
    return board

def changeBoard(board, token, position):
    board[position[0]][position[1]] = token
    return board

def isLegal(board,position):
    if position[0] not in range(3) or position[1] not in range(3):
        return False
    if board[position[0]][position[1]] != '-':
        return False
    return True

def userMoveToMatrixPosition(move):
    row = (move - 1) // 3
    col = (move - 1) % 3
    return (row,col)

def userInput(board):
    num = 100
    while num not in range(1,10):
        num = int(input("Enter number 1-9: "))
        position = userMoveToMatrixPosition(num)
        if isLegal(board,position):
            break
    return position
def getUser():
    user = '-'
    while user not in ('X','O'):
        user = input("Choose either X or O: ")
        user = user.upper()
    return user
def getCPU(user):
    if user == "X":
        return "O"
    else:
        return "X"
def userMove(board, user):
    position = userInput(board)
    board = changeBoard(board,user,position)
    printBoard(board)
    return board

def getLegalMoves(board):
    moves = []
    for rowIndex, row in enumerate(board):
        for colIndex, col in enumerate(row):
            if col == '-':
                moves.append((rowIndex,colIndex))
    return moves
def cpuMove(board,cpu):
    moves = getLegalMoves(board)
    position = moves[random.randint(0,len(moves)-1)]
    board = changeBoard(board,cpu,position)
    printBoard(board)
    return board

def transpose(board):
    transposeBoard = resetBoard()
    for rowIndex, row in enumerate(board):
        for colIndex, value in enumerate(row):
            transposeBoard[colIndex][rowIndex] = value
    return transposeBoard

def getDiagonals(board):
    diag = [ board[i][i] for i in range(len(board)) ]
    counterDiag = [ row[-i-1] for i,row in enumerate(board) ]
    return [diag,counterDiag,[]]

def isOver(board, player):
    transposedBoard = transpose(board)
    diagList = getDiagonals(board)
    for row, col, diag in zip(board, transposedBoard, diagList):
        if row.count(player) == 3 or col.count(player) == 3 or diag.count(player) == 3:
            return True
    return False
    
board = resetBoard()
user = getUser()
cpu = getCPU(user)
gameOver = False
while not gameOver:
    order = ["X","O"]
    for turn in order:
        if user == turn:
            print ('------------ YOUR TURN --------------------')
            print()
            print()
            board = userMove(board,user)
        else:
            print ('------------ CPU TURN ---------------------')
            print()
            print()
            board = cpuMove(board,cpu)
        gameOver = isOver(board, turn)
        if gameOver:
            print ("{} wins!!".format(turn))
            break