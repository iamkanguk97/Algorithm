# BOJ 1260번: DFS와 BFS (S2)

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for next in range(1, n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        curr = q.pop(0)
        print(curr, end=' ')
        for next in range(1, n+1):
            if not visited[next] and graph[curr][next]:
                visited[next] = True
                q.append(next)

n, m, v = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs(v)
print()

visited = [False] * (n+1)
q = [v]
visited[v] = True

bfs()