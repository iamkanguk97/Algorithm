"""
백준 10866 (S4): 덱
https://www.acmicpc.net/problem/10866
"""

from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
queue = deque()  # deque 선언

for _ in range(n):
  command = sys.stdin.readline().rstrip().split(' ')

  if len(command) > 1:
    if command[0] == 'push_front':  # 덱 앞에 넣음
      queue.appendleft(command[1])
    elif command[0] == 'push_back':  # 덱 뒤에 넣음
      queue.append(command[1])
  else:
    if command[0] == 'pop_front':  # 가장 앞에있는 수를 빼고 출력
      if len(queue) == 0:
        print(-1)
      else:
        popData = queue.popleft()
        print(popData)
    elif command[0] == 'pop_back':  # 가장 뒤에있는 수를 빼고 출력
      if len(queue) == 0:
        print(-1)
      else:
        popData = queue.pop()
        print(popData)
    elif command[0] == 'size':  # 정수 개수 출력
      print(len(queue))
    elif command[0] == 'empty':  # 비어있으면 1 아니면 0
      print(1 if len(queue) == 0 else 0)
    elif command[0] == 'front':  # 가장 앞에 있는 정수 출력
      if len(queue) == 0:
        print(-1)
      else:
        print(queue[0])
    elif command[0] == 'back':  # 가장 뒤에 있는 정수 출력
      if len(queue) == 0:
        print(-1)
      else:
        print(queue[-1])
