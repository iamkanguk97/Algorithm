"""
백준 2439 (B4): 별 찍기 - 2
https://www.acmicpc.net/problem/2439
"""

n = int(input())

for i in range(n, 0, -1):
  for j in range(i-1):
    print(' ', end='')
  for j in range(n-i+1):
    print('*', end="")
  print()
  