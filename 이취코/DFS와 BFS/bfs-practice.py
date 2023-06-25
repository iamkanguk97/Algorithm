"""
이취코 DFS/BFS PART2: BFS 기본 예제 연습
"""

from collections import deque

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for n in graph[node]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True

graph = [
    [0],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 7],
    [1, 7]
]

visited = [False] * 9
bfs(graph, visited, 1)