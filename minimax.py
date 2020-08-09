from board import *

def cpuMove(board,cpu,user):
    _, move = minimax(board, cpu, user, cpu)
    board = changeBoard(board,cpu,move)
    printBoard(board)
    return board

def minimax(board, cpu, user, player):
    gameOver, winner = isOver(board)
    if gameOver:
        if winner == cpu:
            return 1, False
        elif winner == user:
            return -1, False
        else:
            return 0, False
    moves = getLegalMoves(board)
    bestMove = moves[0]
    if player == cpu:
        maxEval = -100
        for move in moves:
            board = changeBoard(board, cpu, move)
            value, _ =  minimax(board, cpu, user, user)
            if value > maxEval:
                maxEval = value
                bestMove = move
            board = undoMove(board,move)
        return (maxEval, bestMove)
    elif player == user:
        minEval = 100
        for move in moves:
            board = changeBoard(board, user, move)
            value, _ = minimax(board, cpu, user, cpu)
            if value < minEval:
                minEval = value
            board = undoMove(board,move)
        return (minEval, bestMove)