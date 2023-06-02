"""
백준 2491 (S4): 수열
https://www.acmicpc.net/problem/2491
"""

n = int(input())
data = list(map(int, input().split()))

if n == 1:
  print(1)
  exit(0)

result = 0
upCount = 0
downCount = 0

# 상승세 확인
for i in range(1, n):
  if data[i-1] <= data[i]:
    upCount += 1
  else:
    upCount = 0

  if result < upCount:
    result = upCount

# 감소세 확인
for i in range(1, n):
  if data[i-1] >= data[i]:
    downCount += 1
  else:
    downCount = 0

  if result < downCount:
    result = downCount

print(result + 1)