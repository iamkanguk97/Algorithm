"""
- BOJ 15651: N과 M (3)
- https://www.acmicpc.net/problem/15651
"""

n, m = map(int, input().split(' '))
data = []

def func():
  if len(data) == m:
    print(*data)
    return
  
  for i in range(1, n+1):
    data.append(i)
    func()
    data.pop()

func()