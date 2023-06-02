"""
백준 2491 (S4): 수열
https://www.acmicpc.net/problem/2491
(시간초과 실패)
"""

n = int(input())
data = list(map(int, input().split()))
result = []

for i in range(n-1):
  upCount = 0
  downCount = 0
  tIdx = i
  for j in range(i+1, n):
    if data[tIdx] <= data[j]:
      upCount += 1
      tIdx = j
    else:
      tIdx = i
      break
  for j in range(i+1, n):
    if data[tIdx] >= data[j]:
      downCount += 1
      tIdx = j
    else:
      break

  temp = (upCount, downCount)
  result.append(temp)

result = [max(d) for d in result]
print(max(result) + 1)