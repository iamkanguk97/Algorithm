"""
백준 2979 (B2): 트럭 주차
https://www.acmicpc.net/problem/2979
"""

a, b, c = map(int, input().split())  # 주차 요금 (A: 1대, B: 2대, C: 3대)
time = [list(map(int, input().split())) for _ in range(3)]   # 주차 시간 배열
max_time = max(max(time, key=lambda x: x[1]))   # 제일 마지막까지 있는 시간

check = [0] * (max_time + 1)   # 시간별 주차 상황 저장

# 주차 상황 저장하기
for t in time:
  for i in range(t[0], t[1]):
    check[i] += 1


result = 0
for ch in check:
  if ch == 1:
    result += a
  elif ch == 2:
    result += (b * 2)
  elif ch == 3:
    result += (c * 3)

print(result)