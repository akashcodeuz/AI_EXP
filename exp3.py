#water jug promblem
from collections import deque

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target

    def bfs(self):
        visited = set()
        queue = deque([((0, 0), [])])  # Initial state: both jugs are empty

        while queue:
            (jug1, jug2), path = queue.popleft()

            if (jug1, jug2) in visited:
                continue

            visited.add((jug1, jug2))

            if jug1 == self.target or jug2 == self.target:
                path.append((jug1, jug2))
                return path

            # Operations: Fill jug1, fill jug2, empty jug1, empty jug2,
            # pour from jug1 to jug2, pour from jug2 to jug1
            next_states = [
                ((self.jug1_capacity, jug2), path + [(jug1, jug2)]),  # Fill jug1
                ((jug1, self.jug2_capacity), path + [(jug1, jug2)]),  # Fill jug2
                ((0, jug2), path + [(jug1, jug2)]),  # Empty jug1
                ((jug1, 0), path + [(jug1, jug2)]),  # Empty jug2
                ((jug1 - min(jug1, self.jug2_capacity - jug2), jug2 + min(jug1, self.jug2_capacity - jug2)), path + [(jug1, jug2)]),  # Pour from jug1 to jug2
                ((jug1 + min(jug2, self.jug1_capacity - jug1), jug2 - min(jug2, self.jug1_capacity - jug1)), path + [(jug1, jug2)])  # Pour from jug2 to jug1
            ]

            for state, state_path in next_states:
                if state not in visited:
                    queue.append((state, state_path))

        return []

# Example usage:
jug_problem = WaterJugProblem(4, 3, 2)
solution_path = jug_problem.bfs()

if solution_path:
    print("Solution exists. Path:")
    for idx, (jug1, jug2) in enumerate(solution_path):
        print(f"Step {idx + 1}: Jug 1: {jug1}, Jug 2: {jug2}")
else:
    print("Solution does not exist.")

