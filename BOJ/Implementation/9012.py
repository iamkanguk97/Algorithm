"""
백준 9012 (S4): 괄호
https://www.acmicpc.net/problem/9012
"""

t = int(input())

for _ in range(t):
  test = input()
  stack = []
  result = None

  for w in test:
    if w == '(':
      stack.append(w)
    else:
      if len(stack) != 0:
        stack.pop()
      else:
        result = False
        break

  if result == None:
    result = True if len(stack) == 0 else False
  print('NO' if result == False else 'YES')
