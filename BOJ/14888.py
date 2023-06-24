"""
백준 14888번: 연산자 끼워넣기 (S1)
https://www.acmicpc.net/problem/14888
"""

n = int(input())
data = list(map(int, input().split()))
plus, minus, time, divide = list(map(int, input().split()))

max_v = -1e9
min_v = 1e9

def func(depth, start, plus, minus, time, divide):
  global max_v, min_v

  # 탈출조건
  if depth == n:
    max_v = max(start, max_v)
    min_v = min(start, min_v)
  
  if plus != 0:
    func(depth + 1, start + data[depth], plus-1, minus, time, divide)
  if minus != 0:
    func(depth + 1, start - data[depth], plus, minus-1, time, divide)
  if time != 0:
    func(depth + 1, start * data[depth], plus, minus, time-1, divide)
  if divide != 0:
    func(depth + 1, int(start / data[depth]), plus, minus, time, divide-1)  


func(1, data[0], plus, minus, time, divide)
print(max_v, min_v)