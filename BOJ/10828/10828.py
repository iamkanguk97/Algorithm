# 백준 10828: 스택
# https://www.acmicpc.net/problem/10828
"""
    1. input()을 쓰면 시간초과가 발생할 수 있다. 그렇기 때문에 sys.stdin.readline 사용
    2. 파이썬에서는 stack을 제공X -> list로 구현 가능 -> POP할때 array.pop 메서드가 있는걸 모르고 remove 사용
    3. list의 제일 위 원소는 list[len(list)-1]로도 가능하지만 그냥 list[-1]도 가능하더라..!
"""

import sys 

stack = []
N = int(sys.stdin.readline())

for _ in range(N):
    method = sys.stdin.readline().split()
    
    if method[0] == 'push':
        stack.append(method[1])
    elif method[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif method[0] == 'size':
        print(len(stack))
    elif method[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif method[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])