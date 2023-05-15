n = int(input())
find = int(input())
find_x, find_y = -1, -1  # 찾으려는 값 좌표
matrix = [[0] * n for _ in range(n)]

sx, sy = n // 2, n // 2  # 시작지점 x와 y좌표
matrix[sx][sy] = 1  # 중앙은 1로 설정
num = 2  # 시작 번호
size = 3  # 시작 외각 크기

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while (sx != 0 or sy != 0):
  while num <= size * size:  # 번호가 현재 외각의 크기만큼 할당될때까지
    if sx == sy == (n // 2):  # 현재 외각의 시작좌표
      up, right, down, left = size, size - 2, size - 1, size - 1  # 상하좌우 이동횟수 저장
      sx += dx[0]
      sy += dy[0]
      up -= 1  # 위 횟수 감소
    else:
      if right > 0:  # 오른쪽으로 이동하는 횟수 남은 경우
        sx += dx[3]
        sy += dy[3]
        right -= 1  # 오른쪽 횟수 감소
      elif down > 0:  # 아래로 이동하는 횟수 남은 경우
        sx += dx[1]
        sy += dy[1]
        down -= 1  # 아래로 이동하는 횟수 감소
      elif left > 0:  # 왼쪽으로 이동하는 횟수 남은 경우
        sx += dx[2]
        sy += dy[2]
        left -= 1  # 왼쪽 횟수 감소
      else:  # 위로 이동하는 횟수 남은 경우
        sx += dx[0]
        sy += dy[0]
        up -= 1  # 위 횟수 감소

    matrix[sx][sy] = num  # 숫자 할당
    num += 1  # 숫자 증가

  # 해당 외각에 대한 작업이 끝남
  size += 2  # 외각 사이즈 늘려줌
  n -= 2  # 시작 좌표 변경으로 인해 박스 크기 줄여줌


# 그래프 출력
for i in range(len(matrix)):
  for j in range(len(matrix)):
    print(matrix[i][j], end=" ")
    if matrix[i][j] == find:
      find_x, find_y = i, j
  print()

print(find_x+1, find_y+1)