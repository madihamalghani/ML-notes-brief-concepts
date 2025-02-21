<!-- It is not a perfect game because chosing another row or column will through error( just for understanding or exploring numpy) -->
Using NumPy to implement a **Tic-Tac-Toe** game will help you understand NumPy arrays in a fun and practical way. 

---

## **Step 1: Setting Up the Board**

Since Tic-Tac-Toe is a 3×3 grid, we can represent it as a **NumPy 2D array**.

```python
import numpy as np

# Create a 3x3 board filled with empty spaces
board = np.full((3, 3), ' ')

```

This creates:

```css
[[' ' ' ' ' ']
 [' ' ' ' ' ']
 [' ' ' ' ' ']]

```

We will use:

- `'X'` for Player 1
- `'O'` for Player 2
- `' '` (space) for an empty cell

## **Step 2: Displaying the Board**

To visualize the board, we can define a function:

```python
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

print_board(board)

```

This will display:

```
  |   |
---------
  |   |
---------
  |   |

```

---

## **Step 3: Making a Move**

Players should be able to place `'X'` or `'O'` in an empty cell.

```python
def make_move(board, row, col, player):
    if board[row, col] == ' ':
        board[row, col] = player
        return True  # Move successful
    else:
        print("Invalid move! Try again.")
        return False  # Move failed

```

Example usage:

```python
make_move(board, 0, 1, 'X')  # Player X moves to (0,1)
print_board(board)

```

---

## **Step 4: Checking for a Winner**

We need to check if a player has **won** after each move.

```python
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True

    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

```

How it works:

- `np.all(board[i, :] == player)`: Checks if a row is filled with the same player symbol.
- `np.all(board[:, i] == player)`: Checks if a column is filled.
- `np.diag(board)`: Extracts the main diagonal.
- `np.fliplr(board)`: Flips the board left-to-right to check the **anti-diagonal**.

---

## **Step 5: Checking for a Draw**

If the board is full and no one has won, the game is a draw.

```python

def check_draw(board):
    return np.all(board != ' ')  # If no empty spaces remain

```

---

## **Step 6: Putting It All Together**

Now, let’s create the **game loop**:

```python
def play_game():
    board = np.full((3, 3), ' ')
    players = ['X', 'O']
    turn = 0  # Player index (0 for X, 1 for O)

    while True:
        print_board(board)
        print(f"Player {players[turn]}'s turn.")

        # Get user input
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        # Make a move if valid
        if make_move(board, row, col, players[turn]):
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
            turn = 1 - turn  # Alternate between 0 and 1

```

Run the game with:
```python
play_game()

```