"""
백준 11866 (S5): 요세푸스 문제 0
https://www.acmicpc.net/problem/11866
"""

from collections import deque

n, k = map(int, input().split())
queue = deque([i+1 for i in range(n)])
result = []

while queue:
  for _ in range(k-1):
    queue.append(queue.popleft())
  result.append(queue.popleft())

print('<', end = "")
for i in range(len(result)-1):
  print(str(result[i]) + ', ', end="")
print(result[-1], end="")
print('>')