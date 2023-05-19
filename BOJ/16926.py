"""
백준 16926 (S1): 배열 돌리기1
https://www.acmicpc.net/problem/16926
"""

n, m, r = map(int, input().split())   # n, m: 배열의 크기 / r: 회전의 수
matrix = [list(map(int, input().split())) for _ in range(n)]   # 2차원 배열

for _ in range(r):
  for i in range(min(n, m) // 2):
    sx, sy = i, i   # 시작 x,y좌표
    temp = matrix[sx][sy]   # 임시저장값
    
    # 왼쪽줄
    for j in range(i+1, n-i):
      sx = j   # x좌표 설정
      prev = matrix[sx][sy]   # 값 미리 저장
      matrix[sx][sy] = temp   # 미리 저장되어있던 값 넣기 (이전 값 넣기)
      temp = prev   # 미리 저장하는 곳에 현재값 넣기
    # 아래줄
    for j in range(i+1, m-i):
      sy = j   # y좌표 설정
      prev = matrix[sx][sy]
      matrix[sx][sy] = temp
      temp = prev
    # 오른쪽줄
    for j in range(i+1, n-i):
      sx = n-1-j
      prev = matrix[sx][sy]
      matrix[sx][sy] = temp
      temp = prev
    # 윗줄
    for j in range(i+1, m-i):
      sy = m-1-j
      prev = matrix[sx][sy]
      matrix[sx][sy] = temp
      temp = prev
      
      
for i in range(n):
  for j in range(m):
    print(matrix[i][j], end=" ")
  print()