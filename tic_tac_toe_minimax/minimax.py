
def has_won(board, maximising_player):
    character = "X" if maximising_player else "O"
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == character:
            return True
        if board[i][0] == board[i][1] == board[i][2] == character:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == character:
        return True
    if board[2][0] == board[1][1] == board[0][2] == character:
        return True
    return False

def is_full(board):  # not called is_draw because wins are possible
    return all(c != "-" for row in board for c in row)

def generate_child_boards(board, maximising_player):
    character = "X" if maximising_player else "O"
    # don't ask
    return [board[:y] + [board[y][:x] + [character] + board[y][x+1:]] + board[y+1:]
            for y in range(3) for x in range(3) if board[y][x] == "-"]

def minimax(board, maximising_player):
    if has_won(board, True):
        return 1
    if has_won(board, False):
        return -1
    if is_full(board):
        return 0

    child_boards = generate_child_boards(board, maximising_player)
    evaluations = [minimax(child_board, not maximising_player) for child_board in child_boards]

    if maximising_player:
        return max(evaluations)
    else:
        return min(evaluations)

def calculate_best_child(board, maximising_player):
    child_boards = generate_child_boards(board, maximising_player)
    evaluations = [minimax(child_board, not maximising_player) for child_board in child_boards]

    if maximising_player:
        best_evaluation = max(evaluations)
    else:
        best_evaluation = min(evaluations)
    return child_boards[evaluations.index(best_evaluation)]