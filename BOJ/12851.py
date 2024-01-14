"""
- BOJ 12851: 숨바꼭질2 (G4)
- https://www.acmicpc.net/problem/12851
"""

from collections import deque
subin, brother = map(int, input().split(' '))
visited = [0] * 100001

q = deque([subin])
count, result = 0, 0

while q:
  val = q.popleft()

  if val == brother:
    result = visited[val]
    count += 1
    continue

  for i in [val-1, val+1, val*2]:
    if 0 <= i < 100001 and (visited[i] == 0 or visited[i] == visited[val] + 1):
      visited[i] = visited[val] + 1
      q.append(i)

print(result)
print(count)