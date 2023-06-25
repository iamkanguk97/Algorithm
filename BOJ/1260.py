"""
백준 1260번: DFS와 BFS (S2)
https://www.acmicpc.net/problem/1260
"""

from collections import deque

def dfs(graph, visited, start):
    visited[start] = True
    print(start, end=' ')
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, node)

def bfs(graph, visited, start):
    queue = deque([start])   # 시작노드 삽입
    visited[start] = True   # 해당 노드 방문처리

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for data in graph[node]:
            if not visited[data]:
                queue.append(data)
                visited[data] = True

n, m, v = map(int, input().split())  # n: 정점개수, m: 간선개수, v: 탐색 시작번호
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    graph[a].sort()
    graph[b].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(graph, visited_dfs, v)
print()
bfs(graph, visited_bfs, v)