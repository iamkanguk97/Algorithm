"""
백준 2178번: 미로 탐색 (S1)
https://www.acmicpc.net/problem/2178
"""

from collections import deque

n, m = map(int, input().split())
maze = [[0] * (m+1)] + [[0] + list(map(int, input())) for _ in range(n)]
result = 0

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx <= n and 0 < ny <= m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append([nx, ny])

    return maze[n][m]



print(bfs(1, 1))