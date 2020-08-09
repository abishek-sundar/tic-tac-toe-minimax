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

def undoMove(board, position):
    board[position[0]][position[1]] = '-'
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

def getDiagonals(board):
    diag = [ board[i][i] for i in range(len(board)) ]
    counterDiag = [ row[-i-1] for i,row in enumerate(board) ]
    return [diag,counterDiag,[]]

def isOver(board):
    for player in ['X','O']:
        transposedBoard = transpose(board)
        diagList = getDiagonals(board)
        for row, col, diag in zip(board, transposedBoard, diagList):
            if row.count(player) == 3 or col.count(player) == 3 or diag.count(player) == 3:
                return True, player
    if len(getLegalMoves(board)) == 0:
        return True, '-'
    return False, 0

def transpose(board):
    transposeBoard = resetBoard()
    for rowIndex, row in enumerate(board):
        for colIndex, value in enumerate(row):
            transposeBoard[colIndex][rowIndex] = value
    return transposeBoard

def getLegalMoves(board):
    moves = []
    for rowIndex, row in enumerate(board):
        for colIndex, col in enumerate(row):
            if col == '-':
                moves.append((rowIndex,colIndex))
    return moves
    