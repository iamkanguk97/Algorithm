"""
백준 2615 (S1): 오목
https://www.acmicpc.net/problem/2615
"""

omok = [list(map(int, input().split())) for _ in range(19)]   # 19x19 오목판 입력받음

# 오른쪽, 아래, 오른쪽아래, 오른쪽위
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
  for y in range(19):
    if omok[x][y] != 0:   # 바둑알이 놓여져있는 상태
      baduk = omok[x][y]   # 해당 위치의 바둑돌 (흰색 / 검은색)
      for d in range(4):   # 4개 방향으로 탐색진행
        # 이동한 좌표
        nx = x + dx[d]
        ny = y + dy[d]
        count = 1   # 바둑돌 개수

        while 0 <= nx < 19 and 0 <= ny < 19 and baduk == omok[nx][ny]:
          count += 1
          
          # 오목이 완성되었을때 육목 확인 -> 앞쪽 또는 뒷쪽
          if count == 5:
            if (0 <= nx + dx[d] < 19 and 0 <= ny + dy[d] < 19 and omok[nx + dx[d]][ny + dy[d]] == baduk) or (0 <= x - dx[d] < 19 and 0 <= y - dy[d] < 19 and omok[x - dx[d]][y - dy[d]] == baduk):
              break
            else:
              print(baduk)
              print(x+1, y+1)
              exit(0)
          else:
            # 좌표 추가이동
            nx += dx[d]
            ny += dy[d]
        

print(0)