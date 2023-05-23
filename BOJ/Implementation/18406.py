"""
백준 18406 (B2): 럭키 스트레이트
https://www.acmicpc.net/problem/18406
"""

N = input()  # 문자열로 점수 받음
mid = len(N) // 2

left = N[:mid]
right = N[mid:]

sum_left = sum(list(map(int, left)))
sum_right = sum(list(map(int, right)))

if sum_left == sum_right:
  print('LUCKY')
else:
  print('READY')