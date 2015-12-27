from copy import deepcopy
import math
import random
import gamePlay
from getAllPossibleMoves import getAllPossibleMoves


plusInfinity = float("inf")
minusInfinity = float("-inf")

'''
Minimax has an evaluation function that takes the 'total sum' of: sum of its coins with respect to opponents',
sum of its kings w.r.t opponents'
A move on the board which maximizes total sum is the best move
'''
def evaluation(board):
    # Evaluation function 1
    # Count how many more pieces I have than the opponent
    num_men =0
    num_kings = 0
    num_defended = 0
    value = 0

    # Loop through all board positions
    for piece in range(1, 33):

        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]

        #count of how many men I have versus opponents' men
        if board[x][y].upper() == maxPlayer.upper():
            num_men = num_men + 1

        elif board[x][y].upper() == minPlayer.upper():
            num_men = num_men - 1

        #Count how many kings I have versus opponents' kings
        if board[x][y] == maxPlayer.upper():
            num_kings = num_kings+2

        elif board[x][y] == minPlayer.upper():
            num_kings = num_kings-2

        #count how many pieces are well guarded
        if board[x][y] == maxPlayer.upper():
            try:
                if board[x-1][y+1].upper() == maxPlayer.upper() or board[x+1][y-1].upper() == maxPlayer.upper()\
                   or board[x+1][y+1].upper() == maxPlayer.upper() or board[x-1][y-1].upper() == maxPlayer.upper():
                   num_defended = num_defended + 1
            except IndexError:
                return

    value = num_men + num_kings + num_defended

    return value

#The Minimax Function

def miniMax(board,color, depth,alpha,beta):
    if depth == 0: #terminal board
        moveValue = evaluation(board) #the value for this particular state of board
        return moveValue

    if color == maxPlayer:
        bestValue = minusInfinity
        moves = getAllPossibleMoves(board, color)
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,move)
            moveValue = miniMax(newBoard, gamePlay.getOpponentColor(color), depth-1, alpha, beta)
            bestValue = max(bestValue, moveValue) #compare the moveValue with the bestValue(contains previous moveValue)
            alpha = max(alpha, bestValue) #compares the current bestValue with alpha(contains previous bestValue)
            if beta <= alpha:
                break
        return bestValue

    else:
        bestValue = plusInfinity
        moves = getAllPossibleMoves(board, color)
        for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,move)
            moveValue = miniMax(newBoard, gamePlay.getOpponentColor(color), depth-1, alpha, beta)
            bestValue = min (bestValue, moveValue)#compare the moveValue with the bestValue(contains previous moveValue)
            beta = min(beta, bestValue)#compares the current bestValue with beta(contains previous bestValue)
            if beta <= alpha:
               break
        return bestValue




def nextMove(board, color, time, movesRemaining):

    #vary depth for different time intervals
    if time >= 100:
        depth = 6
    elif time >= 75 and time < 100:
        depth = 5
    elif time >= 37.5 and time < 75:
        depth = 3
    else:
        depth = 2

    #the color that comes to nextMove is always the maxPlayer
    global maxPlayer, minPlayer
    maxPlayer = color
    minPlayer = gamePlay.getOpponentColor(color)

    #initialization for alpha-beta pruning
    alpha = minusInfinity
    beta = plusInfinity

    #Trying to find the move where I have best score
    moves = getAllPossibleMoves(board, color)
    if len(moves) == 1:  #if there is only a jumpmove, return that move
        bestMove = moves[0]
    else:
        best = None
        for move in moves:
                newBoard = deepcopy(board)
                gamePlay.doMove(newBoard,move)
                moveVal = miniMax(newBoard,minPlayer,depth,alpha,beta) # send minPlayer to get best move
                if best == None or moveVal > best:
                    bestMove = move
                    best = moveVal

    return bestMove






