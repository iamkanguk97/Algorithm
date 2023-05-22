"""
이취코 구현 PART2: 게임 개발
난이도: 2
"""

n, m = map(int, input().split())  # n: 세로크기, m: 가로크기
a, b, d = map(int, input().split())  # a,b: 캐릭터가 있는 좌표 / d: 바라보는 방향
map = [list(map(int, input().split())) for _ in range(n)]  # 맵이 육지인지 바다인지
visited = [[0] * m for _ in range(n)]  # 방문확인 배열

# 북/동/남/서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[a][b] = 1  # 처음 위치한 곳 방문 처리


# 왼쪽으로 회전하는 함수
def turn_left():
  global d
  if d == 0:
    d = 3
  else:
    d -= 1


turn_count = 0
result = 0
while True:
  turn_left()  # 왼쪽으로 회전

  # 캐릭터 이동할 곳 좌표 저장
  na = a + dx[d]
  nb = b + dy[d]

  if visited[na][nb] == 0 and map[na][nb] == 0:  # 방문하지 않고 육지인 경우
    visited[na][nb] = 1  # 방문처리
    a, b = na, nb
    turn_count = 0
    continue
  else:
    turn_count += 1

  if turn_count == 4:  # 4방향 다 돌았음
    na = a - dx[d]
    nb = b - dy[d]
    if map[na][nb] == 0:   # 뒤로 이동하는데 육지이면 이동 가능
      a, b = na, nb
    else:
      break
    turn_count = 0

for v in visited:
  result += v.count(1)
print(result)
