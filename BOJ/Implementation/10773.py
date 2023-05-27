"""
백준 10773 (S4): 제로
https://www.acmicpc.net/problem/10773
"""

k = int(input())   # 정수
stack = []

for _ in range(k):
  data = int(input())
  if data != 0:   # 0이 아니면 stack에 넣음
    stack.append(data)
  else:   # 0이면 맨 위의 데이터 버림
    stack.pop()

print(sum(stack))