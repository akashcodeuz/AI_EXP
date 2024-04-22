# #experiment for implmentation of BFS and DFS
# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)

#     while queue:
#         vertex = queue.popleft()
#         print(vertex, end=" ")

#         for neighbor in graph[vertex]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)

# # Example graph represented as an adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# print("BFS traversal starting from vertex 'A':")
# bfs(graph, 'A')
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS traversal starting from vertex 'A':")
dfs(graph, 'A')
