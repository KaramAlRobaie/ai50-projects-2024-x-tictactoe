"""
Tic Tac Toe Player
"""

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter = {"X":0, "O":0}
    for row in board:
        for square in row:
            if square != EMPTY:
                counter[square] += 1

    return "X" if counter["X"] == counter["O"] else "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return_set = []
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square == EMPTY:
                return_set.append((i, j))

    return return_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    return_board = deepcopy(board)
    i, j = action
    if return_board[i][j] != EMPTY:
        raise IndexError
    else:
        return_board[i][j] = player(board)
    
    return return_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row_or_column in range(3):
        if board[row_or_column][0] == board[row_or_column][1] == board[row_or_column][2]:
            return board[row_or_column][0]
        elif board[0][row_or_column] == board[1][row_or_column] == board[2][row_or_column]:
            return board[0][row_or_column]
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        return board[1][1]   
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for row in board:
            for square in row:
                if square == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == "X":
        return 1
    elif result == "O":
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """  
    if terminal(board):
        return None
    
    if player(board) == "X":
        _, move = max_return(board)
        return move
    else:
        _, move = min_return(board)
        return move
    


def max_return(board):
    if terminal(board):
        return (utility(board), None)

    max_value = float('-inf')
    optimal_action = None

    for action in actions(board):
        value, move = min_return(result(board, action))
        if value > max_value:
            if value == 1:
                return (value, move)
            optimal_action = action
            max_value = value
    
    return (max_value, optimal_action)

def min_return(board):
    if terminal(board):
        return (utility(board), None)
    
    min_value = float('inf')
    optimal_action = None

    for action in actions(board):
        value, move = max_return(result(board, action))
        if value < min_value:
            if value == -1:
                return (value, move)
            optimal_action = action
            min_value = value
    
    return (min_value, optimal_action)

            



    
