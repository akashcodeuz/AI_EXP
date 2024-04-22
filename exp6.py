#a* alogarthim using 
import heapq

class Node:
    def __init__(self, state, parent=None, action=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def is_goal(self, goal_state):
        return self.state == goal_state

    def get_neighbors(self):
        neighbors = []
        zero_index = self.state.index(0)
        row, col = zero_index // 3, zero_index % 3
        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = list(self.state)
                new_index = new_row * 3 + new_col
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(Node(tuple(new_state), self, move, self.depth + 1, self.cost + 1))
        return neighbors

    def heuristic(self):
        # Manhattan distance heuristic
        return sum(abs(val // 3 - idx // 3) + abs(val % 3 - idx % 3)
                   for idx, val in enumerate(self.state) if val != 0)

def a_star_search(initial_state, goal_state):
    start_node = Node(initial_state)
    goal_node = Node(goal_state)
    open_list = [start_node]
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.is_goal(goal_state):
            # Goal reached, reconstruct the path
            path = []
            while current_node:
                path.append((current_node.state, current_node.action))
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        for neighbor in current_node.get_neighbors():
            if neighbor not in closed_set and neighbor not in open_list:
                heapq.heappush(open_list, neighbor)

    return None  # No solution found

if __name__ == "__main__":
    initial_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    path = a_star_search(initial_state, goal_state)

    if path:
        print("Optimal Path:")
        for state, action in path:
            print(f"State: {state}, Action: {action}")
    else:
        print("No solution found.")
