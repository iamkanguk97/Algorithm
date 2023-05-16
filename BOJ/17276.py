"""
백준 17276 (S2): 배열 돌리기
https://www.acmicpc.net/problem/17276
"""

def rotate(matrix, n, d):
  rotate_count = abs(d) // 45   # 회전 횟수

  for _ in range(rotate_count):
    temp_list = []
    if d > 0:
      # (0) 주대각선 데이터 받아옴
      for i in range(n):
        temp_list.append(matrix[i][i])

      # (1) 주대각선에서 가운데로 이동
      for i in range(n):
        temp_data = matrix[i][n//2]   # 가운데 데이터
        matrix[i][n//2] = temp_list[i]   # temp_list에 저장되어있던 주대각선 데이터를 가운데로 이동시킴
        temp_list[i] = temp_data   # 가운데에 저장되어있던 데이터 temp_list에 저장
    
      # (2) 가운데에서 부대각선으로
      for i in range(n):
        temp_data = matrix[i][n-1-i]   # 부대각선 데이터
        matrix[i][n-1-i] = temp_list[i]   # temp_list에 저장되어있던 가운데 데이터를 부대각선으로 이동
        temp_list[i] = temp_data   # 부대각선 데이터 temp_list에 저장
    
      # (3) 부대각선에서 가운데-가로로
      for i in range(n):
        temp_data = matrix[n//2][n-1-i]   # 가운데-가로 데이터
        matrix[n//2][n-1-i] = temp_list[i]   # temp_list에 저장되어있던 부대각선 데이터를 가운데-가로로 이동
        temp_list[i] = temp_data   # 가운데-가로 데이터 temp_list에 저장

      # (4) 가운데-가로에서 주대각선으로
      for i in range(n):
        matrix[n-1-i][n-1-i] = temp_list[i]
    else:
      # (0) 주대각선 데이터 받아옴
      for i in range(n):
        temp_list.append(matrix[i][i])

      # (1) 주대각선에서 가운데-가로로 이동
      for i in range(n):
        temp_data = matrix[n//2][i]   # 가운데-가로 데이터
        matrix[n//2][i] = temp_list[i]   # temp_list에 저장되어있던 주대각선 데이터를 가운데-가로로 이동시킴
        temp_list[i] = temp_data   # 가운데-가로에 저장되어있던 데이터 temp_list에 저장
    
      # (2) 가운데-가로에서 부대각선으로
      for i in range(n):
        temp_data = matrix[n-1-i][i]   # 부대각선 데이터
        matrix[n-1-i][i] = temp_list[i]   # temp_list에 저장되어있던 가운데-가로 데이터를 부대각선으로 이동
        temp_list[i] = temp_data   # 부대각선 데이터 temp_list에 저장
    
      # (3) 부대각선에서 가운데-가로로
      for i in range(n):
        temp_data = matrix[n-1-i][n//2]   # 가운데-가로 데이터
        matrix[n-1-i][n//2] = temp_list[i]   # temp_list에 저장되어있던 부대각선 데이터를 가운데-가로로 이동
        temp_list[i] = temp_data   # 가운데-가로 데이터 temp_list에 저장

      # (4) 가운데-가로에서 주대각선으로
      for i in range(n):
        matrix[n-1-i][n-1-i] = temp_list[i]


  return matrix

t = int(input())  # 테스트 케이스 수

for i in range(t):
  n, d = map(int, input().split())  # n: 배열의 크기, d: 각도
  matrix = [list(map(int, input().split(' '))) for _ in range(n)]
  rotated_matrix = rotate(matrix, n, d)   # 회전

  for i in range(n):
    for j in range(n):
      print(rotated_matrix[i][j], end = ' ')
    print()