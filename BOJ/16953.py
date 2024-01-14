"""
- BOJ 16953: A->B (S2)
- https://www.acmicpc.net/problem/16953
"""

from collections import deque

a, b = map(int, input().split(' '))
queue = deque([(a, 1)])

isFind = False
while queue:
  value, count = queue.popleft()
  if value == b:
    isFind = True
    print(count)
    break

  if value > b:
    continue

  queue.append((value * 2, count + 1))
  queue.append((value * 10 + 1, count + 1))


if isFind == False:
  print(-1)