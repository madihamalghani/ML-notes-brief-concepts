# with complete functionality:
import numpy as np

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def make_move(board, cell_number, player):
    row, col = (cell_number - 1) // 3, (cell_number - 1) % 3  # Convert 1-9 to (row, col)

    if board[row, col] == ' ':
        board[row, col] = player
        return True  # Move successful
    else:
        print("Invalid move! Cell is already occupied. Try again.")
        return False  # Move failed

def check_winner(board, player):
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True

    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def check_draw(board):
    return np.all(board != ' ')  # Returns True if the board is full

def play_game():
    board = np.full((3, 3), ' ')
    players = ['X', 'O']
    turn = 0  

    while True:
        print_board(board)
        print(f"Player {players[turn]}'s turn.")

        while True:  # Input validation loop
            try:
                cell_number = int(input("Enter a cell number (1-9): "))

                if cell_number not in range(1, 10):  # Check if input is within range
                    print("Invalid input! Please enter a number between 1 and 9.")
                    continue

                if make_move(board, cell_number, players[turn]):  # Check if move is valid
                    break  # Exit input loop if move is successful

            except ValueError:
                print("Invalid input! Please enter a number.")

        # Check for a winner
        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Player {players[turn]} wins!")
            break

        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch turn
        turn = 1 - turn  

# Run the game
play_game()
