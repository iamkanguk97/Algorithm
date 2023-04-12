# DFS와 BFS PART2 실전문제) 미로탈출
from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 상하좌우 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque() # BFS를 위해 Queue 선언
    queue.append((x, y))

    while queue:
        x, y = queue.popleft() 
        
        # 현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어난 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            # 위치가 벽일 경우
            if maze[nx][ny] == 0:
                continue
            
            # 이동이 가능한 경우
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 # 이전 값을 더해준다
                queue.append((nx, ny))

    return maze[N-1][M-1]


print(bfs(0, 0))