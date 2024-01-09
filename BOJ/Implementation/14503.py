"""
- BOJ G5: 로봇 청소기 (14503)
- https://www.acmicpc.net/problem/14503
"""

# 북->동->남->서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
room = [list(map(int, input().split(' '))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

visited[r][c] = 1    # 처음 위치한 자리 청소 처리
cleanCount = 1

while True:
  isChecked = False

  for _ in range(4):
    nd = (d + 3) % 4   # 왼쪽으로 이동
    nx = r + dx[nd]
    ny = c + dy[nd]

    # 청소되지 않은 빈칸이 있는 경우 -> 청소가 가능한 경우
    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and room[nx][ny] == 0:
      d = nd   # 반시계 방향으로 90도 회전
      cleanCount += 1   # 청소한 칸 개수 추가
      r, c = nx, ny   # 이동
      visited[nx][ny] = 1
      isChecked = True
      break
    else:
      d = nd

  if isChecked == False:
    nnd = (d + 2) % 4
    nnx = r + dx[nnd]
    nny = c + dy[nnd]

    if room[nnx][nny] == 1:
      break
    else:
      r, c = nnx, nny

print(cleanCount)