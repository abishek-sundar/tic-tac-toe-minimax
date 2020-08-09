from board import *

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