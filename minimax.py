from board import *

def cpuMove(board,cpu,user):
    _, move, _, _= minimax(board, cpu, user, cpu, -100, +100)
    board = changeBoard(board,cpu,move)
    printBoard(board)
    return board

def minimax(board, cpu, user, player, alpha, beta):
    gameOver, winner = isOver(board)
    if gameOver:
        if winner == cpu:
            return 1, False, 0, 0
        elif winner == user:
            return -1, False, 0,0 
        else:
            return 0, False, 0,0 
    moves = getLegalMoves(board)
    bestMove = moves[0]
    if player == cpu:
        maxEval = -100
        for move in moves:
            board = changeBoard(board, cpu, move)
            value, _, _, _ =  minimax(board, cpu, user, user, alpha, beta)
            if value > maxEval:
                maxEval = value
                bestMove = move
            alpha = max(alpha, value)
            board = undoMove(board,move)
        return (maxEval, bestMove, 0, 0)
    elif player == user:
        minEval = 100
        for move in moves:
            board = changeBoard(board, user, move)
            value, _, _, _ = minimax(board, cpu, user, cpu,alpha,beta)
            minEval = min(minEval, value)
            beta = min(beta,value)
            board = undoMove(board,move)
        return (minEval, bestMove, 0, 0)