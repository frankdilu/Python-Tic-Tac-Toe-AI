"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

possiblesBoards = 0
def initial_state():
    """
    Returns starting state of the board.
    """
    global possiblesBoards
    possiblesBoards = 0
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    totalEmpty = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                totalEmpty += 1

    if (totalEmpty % 2) == 0:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = set()
    for i, rows in enumerate(board):
        for j, cell  in enumerate(rows):
            if cell == EMPTY:
                possibleMoves.add((i,j))
    return possibleMoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    if boardCopy[action[0]][action[1]] != EMPTY:
        raise NameError("ImpossibleMove")
    else:
        boardCopy[action[0]][action[1]] = player(boardCopy)
    return boardCopy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != EMPTY:
        return board[2][0]
    
    # Vertical
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != EMPTY:
        return board[0][2]

    # Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if board[0].count(EMPTY) == 0 and board[1].count(EMPTY) == 0 and board[2].count(EMPTY) == 0:
        return True
    elif winner(board) != None:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError

def optimalMove(board, wantedResult):
    global possiblesBoards
    possibleMoves = []
    for action in actions(board):
        resultBoard = result(board, action)
        possiblesBoards += 1
        if terminal(resultBoard):
            return [action, utility(resultBoard)]
        else:
            possibleMoves.append([action,optimalMove(resultBoard, -wantedResult)[1]])
    
    if wantedResult == 1:
        bestMove = max(possibleMoves, key = lambda k: k[1])
        return bestMove
    else:
        bestMove = min(possibleMoves, key = lambda k: k[1])
        return bestMove


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        wantedResult = 1
    else:
        wantedResult = -1

    move = optimalMove(board, wantedResult)

    return move[0]

