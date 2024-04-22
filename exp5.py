#missnary cannible promblem
from queue import Queue

def is_valid_state(missionaries, cannibals):
    # Check if the state is valid (cannibals do not outnumber missionaries)
    return missionaries >= 0 and cannibals >= 0 and (missionaries == 0 or missionaries >= cannibals) \
           and ((3 - missionaries) == 0 or (3 - missionaries) >= (3 - cannibals))

def get_next_states(state):
    # Generate possible next states based on valid moves
    next_states = []
    missionaries, cannibals, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for move in moves:
        dm, dc = move
        if boat == 0:
            new_state = (missionaries - dm, cannibals - dc, 1)
        else:
            new_state = (missionaries + dm, cannibals + dc, 0)
        if is_valid_state(new_state[0], new_state[1]):  # Pass missionaries and cannibals separately to is_valid_state
            next_states.append(new_state)
    return next_states

def missionary_cannibal_bfs():
    # Initialize queue for BFS
    queue = Queue()
    # Initial state: 3 missionaries, 3 cannibals, and boat on the original side
    initial_state = (3, 3, 0)
    # Enqueue the initial state along with the path
    queue.put((initial_state, []))

    while not queue.empty():
        current_state, path = queue.get()
        # Check if the goal state is reached
        if current_state == (0, 0, 1):
            return path
        # Generate possible next states
        next_states = get_next_states(current_state)
        for next_state in next_states:
            # Enqueue the next state along with the updated path
            queue.put((next_state, path + [next_state]))
    return None  # If the goal state cannot be reached

if __name__ == "__main__":
    result_path = missionary_cannibal_bfs()
    if result_path:
        print("Solution found:")
        for i, state in enumerate(result_path):
            print(f"Step {i + 1}: {state}")
    else:
        print("No solution found.")
