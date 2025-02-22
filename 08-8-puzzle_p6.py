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
            moved_tile = state[new_pos]  # Find which tile moved
            neighbors.append((new_state, move, moved_tile))
    
    return neighbors

def bfs_solver(start_state):
    """Solve the 8-puzzle using Breadth-First Search (BFS)."""
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(tuple(start_state.flatten()))
    
    while queue:
        current_state, path = queue.popleft()
        
        print("\nStep:", len(path))
        print(current_state)
        
        if np.array_equal(current_state, goal_state):
            return path
        
        for neighbor, move, moved_tile in get_neighbors(current_state):
            state_tuple = tuple(neighbor.flatten())
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((neighbor, path + [(move, moved_tile)]))
    
    return None  # No solution found

# Example Start State
start_state = np.array([[7, 2, 4],
                         [5, 0, 6],
                         [8, 3, 1]])

# Solve the puzzle
solution = bfs_solver(start_state)
print("Solution Moves:", solution)

# Apply moves to show each step result
if solution:
    current_state = start_state.copy()
    for step, (move, moved_tile) in enumerate(solution, 1):
        for neighbor, neighbor_move, neighbor_tile in get_neighbors(current_state):
            if neighbor_move == move and neighbor_tile == moved_tile:
                current_state = neighbor
                print(f"\nMove {step}: {move} (Tile {moved_tile} moved)")
                print(current_state)
                break
