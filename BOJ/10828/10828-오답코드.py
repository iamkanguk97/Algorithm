# 백준 10828: 스택
# https://www.acmicpc.net/problem/10828
# 내가풀은... 오답코드 ㅠㅠ

stack = []
result = []
N = int(input())

for i in range(N):
    method = input()
    
    if method.split(' ')[0] == 'push':   # PUSH: 정수 X를 스택에 넣는 연산
        stack.append(method.split(' ')[1])
    else:
        if method == 'pop':   # POP: 스택에서 가장 위에 있는 정수를 출력. 스택에 들어있는 정수가 없으면 -1 출력
            if len(stack) == 0:   # 스택에 들어있는 정수가 없음
                result.append(-1)
            else:
                popData = stack[len(stack) - 1] 
                stack.remove(popData)   # 가장 위에있는 정수를 뺌
                result.append(popData)
        elif method == 'size':   # SIZE: 스택에 들어있는 정수의 개수를 출력
            result.append(len(stack))
        elif method == 'empty':   # EMPTY: 스택이 비어있으면 1, 아니면 0을 출력
            if len(stack) == 0:
                result.append(1)
            else:
                result.append(0)
        elif method == 'top':   # TOP: 스택의 가장 위에 있는 정수를 출력. 스택에 들어있는 정수가 없으면 -1 출력
            if len(stack) == 0:   # 스택에 들어있는 정수가 없음
                result.append(-1)
            else:
                result.append(stack[len(stack) - 1])


for i in range(len(result)):
    print(result[i], end = '\n')