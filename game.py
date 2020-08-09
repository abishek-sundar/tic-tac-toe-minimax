import random
from minimax import *
from board import *
from decisions import *

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
            board = cpuMove(board,cpu,user)
        gameOver, winner = isOver(board)
        if gameOver:
            if winner == '-':
                print ("Game tied!")
            else:
                print ("{} wins!!".format(winner))
            break