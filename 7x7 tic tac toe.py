# Tic Tac Toe game for 7x7 board

# Initialize the board with all empty cells
board = [[' ' for j in range(7)] for i in range(7)]

# Define the function to print the board
def print_board():
    for row in board:
        print(' | '.join(row))

# Define the function to check if there's a winner
def check_winner(player):
    # Check rows for a win
    for i in range(7):
        for j in range(4):
            if all([board[i][j+k] == player for k in range(4)]):
                return True
    # Check columns for a win
    for i in range(4):
        for j in range(7):
            if all([board[i+k][j] == player for k in range(4)]):
                return True
    # Check east-south diagonal for a win
    for i in range(4):
        for j in range(4):
            if all([board[i+k][j+k] == player for k in range(4)]):
                return True
    # Check west-south diagonal for a win
    for i in range(4):
        for j in range(3, 7):
            if all([board[i+k][j-k] == player for k in range(4)]):
                return True
    return False

def evaluate_board():
    # Evaluate the board by counting the number of 3-in-a-row for each player and get a score
    x_3_in_a_row = o_3_in_a_row = 0
    for i in range(7): # row wise
        for j in range(4):
            if 'X' in [board[i][j+k] for k in range(4)] and ' ' in [board[i][j+k] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i][j+k] for k in range(4)] and ' ' in [board[i][j+k] for k in range(4)]:
                o_3_in_a_row += 1
    for i in range(4): # col wise
        for j in range(7):
            if 'X' in [board[i+k][j] for k in range(4)] and ' ' in [board[i+k][j] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i+k][j] for k in range(4)] and ' ' in [board[i+k][j] for k in range(4)]:
                o_3_in_a_row += 1
    for i in range(4): # east-south diagonal wise
        for j in range(4):
            if 'X' in [board[i+k][j+k] for k in range(4)] and ' ' in [board[i+k][j+k] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i+k][j+k] for k in range(4)] and ' ' in [board[i+k][j+k] for k in range(4)]:
                o_3_in_a_row += 1
    for i in range(4): # west-south diagonal wise
        for j in range(3, 7):
            if 'X' in [board[i+k][j-k] for k in range(4)] and ' ' in [board[i+k][j-k] for k in range(4)]:
                x_3_in_a_row += 1
            elif 'O' in [board[i+k][j-k] for k in range(4)] and ' ' in [board[i+k][j-k] for k in range(4)]:
                o_3_in_a_row += 1

    if x_3_in_a_row > o_3_in_a_row:
        return 1
    elif o_3_in_a_row > x_3_in_a_row:
        return -1
    else: return 0

# Define the function to play the game
def play_game():
    # Initialize player and turn count
    player = 'X'
    turn_count = 0
    # Loop until a winner is found or the board is full
    while turn_count < 49:
        # Print the board
        print_board()
        if player == 'X':
            # Use minimax with alpha-beta pruning to find the best move for player X
            _, row, col = minimax_alpha_beta(player, -float('inf'), float('inf'), 4)
            print("Player X's move: ({}, {})".format(row, col))
        else:
            # Ask player O for their move
            move = input("Player O, enter your move (row,column): ")
            row, col = map(int, move.split(','))
        # Check if the move is valid and update the board
        if board[row][col] == ' ':
            board[row][col] = player
            # Check if the player has won
            if check_winner(player):
                print_board()
                print("Player " + player + " wins!")
                return
            # Switch to the other player
            player = 'O' if player == 'X' else 'X'
            turn_count += 1
        else:
            print("Invalid move. Try again.")
    # If the loop finishes without a winner, it's a tie
    print_board()
    print("It's a tie!")

# define the minimax function using alpha-beta pruning
def minimax_alpha_beta(player, alpha, beta, depth):
    # base case: check if game has ended or has reached the maximum depth (no moves left)
    if check_winner('X'):
        return 1, None, None
    elif check_winner('O'):
        return -1, None, None
    elif depth == 0:
        return evaluate_board(), None, None

    # maximize player (player 'X')
    if player == 'X':
        best_score = -float('inf')
        best_row = best_col = None

        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score, _, _ = minimax_alpha_beta('O', alpha, beta, depth - 1) # running alpha beta
                    board[i][j] = ' '  # undoing move

                    if score > best_score:
                        best_score = score
                        best_row, best_col = i, j
                    alpha = max(alpha, best_score)

                    if beta <= alpha:
                        break

        return best_score, best_row, best_col

    # minimize player (player 'O')
    else:
        best_score = float('inf')
        best_row = best_col = None

        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score, _, _ = minimax_alpha_beta('X', alpha, beta, depth - 1) # running alpha beta
                    board[i][j] = ' '  # undoing move

                    if score < best_score:
                        best_score = score
                        best_row, best_col = i, j
                    beta = min(beta, best_score)

                    if beta <= alpha:
                        break
        return best_score, best_row, best_col


# start the game
play_game()