This code will provide you the moves, not their structure. Structure is in python  file 08

### **1. Understanding the 8-Puzzle Game**

- We have a **3x3 grid** with **8 numbered tiles** and **one empty space (0)**.
- We can move tiles **into the empty space** (Up, Down, Left, Right).
- The goal is to reach this final arrangement:
    
    ```
    
    0  1  2
    3  4  5
    6  7  8
    
    ```
    
- Example **Start State** in the code:
    
    ```
    7  2  4
    5  0  6
    8  3  1
    ```
    

---

### **2. Setting Up the Code:**

### **a) Define the Goal State**

```python
goal_state = np.array([[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8]])  # 0 represents the empty space

```

- This tells the program what the **final correct arrangement** should be.

### **b) Define Possible Moves**

```python

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

```

- Defines the **four possible moves**.
- Each move changes the **row or column index** of `0`.

---

**Explanation:**

### **How the Moves Work**

The `moves` dictionary helps us move in the **grid** by changing row and column indices.

### **Example Move Explanations:**

1. **'up': (-1, 0)**
    - `1` means **go one row up** (decrease row index).
    - `0` means **stay in the same column**.
    - Example: Moving **up** from `(1,1)` goes to `(0,1)` (from 5 to 2).
2. **'down': (1, 0)**
    - `1` means **go one row down** (increase row index).
    - `0` means **stay in the same column**.
    - Example: Moving **down** from `(1,1)` goes to `(2,1)` (from 5 to 8).
3. **'left': (0, -1)**
    - `0` means **stay in the same row**.
    - `1` means **go one column left** (decrease column index).
    - Example: Moving **left** from `(1,1)` goes to `(1,0)` (from 5 to 4).
4. **'right': (0, 1)**
    - `0` means **stay in the same row**.
    - `1` means **go one column right** (increase column index).
    - Example: Moving **right** from `(1,1)` goes to `(1,2)` (from 5 to 6).

---

### **3. Finding & Swapping Tiles**

### **a) Find the Empty Space (0)**

```python
def find_zero(puzzle):
    return tuple(np.argwhere(puzzle == 0)[0])

```

- **Finds where `0` is located** in the grid.

### **b) Swap Two Tiles**

```python
def swap_positions(puzzle, pos1, pos2):
    new_puzzle = np.copy(puzzle)
    new_puzzle[pos1], new_puzzle[pos2] = new_puzzle[pos2], new_puzzle[pos1]
    return new_puzzle

```

- Makes a **copy** of the grid.
- **Swaps** `0` with an adjacent tile to make a move.

---

### **4. Generating Possible Moves**

```python
def get_neighbors(state):
    neighbors = [] 
    zero_pos = find_zero(state)

    for move, (dx, dy) in moves.items(): 
        new_pos = (zero_pos[0] + dx, zero_pos[1] + dy)

        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_state = swap_positions(state, zero_pos, new_pos)
            neighbors.append((new_state, move))

    return neighbors

```

- **Finds where `0` can move**.
- **Swaps `0`** with the tile in the new position.
- **Returns all possible new states**.

**Explanation:**

This function finds all possible states that can be reached by moving the **zero (0) tile** in a **3×3 grid**

---

### **Step-by-Step Explanation**

### **1️⃣ Find the Position of Zero (`0`)**

```python
zero_pos = find_zero(state)

```

- The function `find_zero(state)` finds **where the zero is** in the 3×3 grid.
- Example:
    
    ```
    
    1  2  3
    4  0  5   <- zero is at (1,1)
    6  7  8
    
    ```
    

### **2️⃣ Loop Through Possible Moves**

```python

for move, (dx, dy) in moves.items():

```

- The `moves` dictionary tells us how **zero can move** (up, down, left, right).
    
    ```python
    
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    
    ```
    
- Each move is represented by **(dx, dy)** (change in row and column):
    - `'up': (-1, 0)` → move up **1 row**
    - `'down': (1, 0)` → move down **1 row**
    - `'left': (0, -1)` → move left **1 column**
    - `'right': (0, 1)` → move right **1 column**

### **3️⃣ Calculate the New Position of Zero**

```python

new_pos = (zero_pos[0] + dx, zero_pos[1] + dy)

```

- `zero_pos[0]` is the **current row**.
- `zero_pos[1]` is the **current column**.
- `(dx, dy)` is added to move zero in the grid.
    
    **Example (Moving Up from (1,1)):**
    
    ```
    
    Current position: (1,1)
    Move up: (-1,0)
    New position: (1-1, 1+0) = (0,1)
    
    ```
    

### **4️⃣ Check If Move is Valid**

```python
if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:

```

- Ensures **zero doesn’t move outside** the 3×3 grid.
- Since our grid is **indexed from 0 to 2**, `new_pos` must be between **0 and 2** for both row and column.
    
    **Example (Invalid Move from (0,1)):**
    
    ```
    Move up (-1,0) → New position (-1,1)
    -1 is out of bounds! ❌
    
    ```
    

### **5️⃣ Swap Zero with the New Position**

```python

new_state = swap_positions(state, zero_pos, new_pos)

```

- Calls a helper function `swap_positions()` to **swap** zero with the new tile.
- This creates a **new state** of the puzzle.

### **6️⃣ Store the New State and Move Direction**

```python

neighbors.append((new_state, move))

```

- The `neighbors` list stores:
    - The **new puzzle state** after the move.
    - The **direction** of the move (`'up'`, `'down'`, etc.).

---

### **5. Solving the Puzzle Using BFS**

```python
def bfs_solver(start_state):
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(tuple(start_state.flatten())) #coverting to 1D array

    while queue:
        current_state, path = queue.popleft() #This takes the next state to explore from the front of the line.
 
        print("\nStep:", len(path))
        print(current_state)

        if np.array_equal(current_state, goal_state):
            return path

        for neighbor, move in get_neighbors(current_state):
            state_tuple = tuple(neighbor.flatten())
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((neighbor, path + [move]))

    return None

#@madihamalghani
```

- **Breadth-First Search (BFS)** finds the shortest solution.
- It keeps track of:
    - **States already visited** (to avoid repeating moves).
    - **Steps taken so far**.
- **If the goal state is found, it stops** and returns the moves.

---

### **6. Running the Solver**

```python

start_state = np.array([[7, 2, 4],
                         [5, 0, 6],
                         [8, 3, 1]])

solution = bfs_solver(start_state)
print("Solution Moves:", solution)

```

- **Starts from a shuffled state**.
- Calls `bfs_solver()` to find the moves needed.
- **Prints each step & final solution**.

**Explanation:**

**BFS** is an algorithm used for searching or traversing through a structure (like a maze, graph, or puzzle) in a **level-by-level** order. It explores all nodes (or states) at a given depth before moving to the next level. This way, if a solution exists, BFS will always find the **shortest path** (in terms of the number of moves).

- **`deque([(start_state, [])])`:**
    
    This is like putting your starting room in a line with an empty record of moves.
    
- **`visited.add(tuple(start_state.flatten()))`:**
    
    This converts the state into a simple format (like a list of numbers) so you can easily check if you’ve been in that room before.
    
- **`queue.popleft()`:**
    
    This takes the next state to explore from the front of the line.
    
- **`if np.array_equal(current_state, goal_state): return path`:**
    
    This checks if you’re at the exit (goal) and if so, returns how you got there.
    
- **`get_neighbors(current_state)`:**
    
    This finds all the moves (doors) you can take from the current state.
    
- **`queue.append((neighbor, path + [move]))`:**
    
    This adds the new state (room) and the updated list of moves (your path) to the end of the line.
    

### **Final Output Example**

```

Step: 0
[[7 2 4]
 [5 0 6]
 [8 3 1]]

Step: 1
[[7 0 4]
 [5 2 6]
 [8 3 1]]

Step: 2
[[0 7 4]
 [5 2 6]
 [8 3 1]]

...

Solution Moves: ['left', 'up', 'right', ...]

```

---

### **Summary**

- **Finds `0`**, swaps it with adjacent tiles.
- **Uses BFS** to explore all possible moves.
- **Finds the shortest path** to the goal state.

---

## Complete Code:

```css
import numpy as np
from collections import deque

# Define goal state
goal_state = np.array([[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8]])  # 0 represents the empty space

# Define possible moves (Up, Down, Left, Right)
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def find_zero(puzzle):
    """Find the position of zero (empty space) in the puzzle."""
    return tuple(np.argwhere(puzzle == 0)[0])

def swap_positions(puzzle, pos1, pos2):
    """Swap two positions in the NumPy array."""
    new_puzzle = np.copy(puzzle)
    new_puzzle[pos1], new_puzzle[pos2] = new_puzzle[pos2], new_puzzle[pos1]
    return new_puzzle

def get_neighbors(state):
    """Generate possible states by moving the empty space."""
    neighbors = []
    zero_pos = find_zero(state)
    
    for move, (dx, dy) in moves.items():
        new_pos = (zero_pos[0] + dx, zero_pos[1] + dy)
        
        if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
            new_state = swap_positions(state, zero_pos, new_pos)
            neighbors.append((new_state, move))
    
    return neighbors

def bfs_solver(start_state):
    """Solve the 8-puzzle using Breadth-First Search (BFS)."""
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(tuple(start_state.flatten()))
    
    while queue:
        current_state, path = queue.popleft()
        
        if np.array_equal(current_state, goal_state):
            return path
        
        for neighbor, move in get_neighbors(current_state):
            state_tuple = tuple(neighbor.flatten())
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((neighbor, path + [move]))
    
    return None  # No solution found

# Example Start State
start_state = np.array([[7, 2, 4],
                         [5, 0, 6],
                         [8, 3, 1]])

# Solve the puzzle
solution = bfs_solver(start_state)
print("Solution Moves:", solution)  
```