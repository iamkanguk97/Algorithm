# BOJ 1012번: 유기농 배추 (S2)
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global graph
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == True:
            graph[ny][nx] = False
            dfs(nx, ny)
    

t = int(input())   # 테스트 케이스 개수
result = []

for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())   # m: 가로길이, n: 세로길이, k: 배추개수
    graph = [[False] * m for _ in range(n)]  # 배추밭 세팅
    for _ in range(k):
        x, y = map(int, input().split())   # 배추 위치 설정
        graph[y][x] = True
    for i in range(m):
        for j in range(n):
            if graph[j][i] == True:
                dfs(i, j)
                count += 1
    result.append(count)

for i in range(len(result)):
    print(result[i])