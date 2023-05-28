def solution(s):
    stack = []   # stack 선언
    for data in s:
        if data == '(':
            stack.append(data)
        else:
            if len(stack) == 0:   # stack이 비어있으면 (가 나온적이 없다는 뜻 -> 에러 발생
                return False
            else:   # (가 저장된 적이 있기 때문에 괄호 생성가능 -> stack에서 제거
                stack.pop()
    
    # 반복문에서 문자열 길이만큼 순회 후 stack이 비어있지 않으면 False
    if len(stack) != 0:
        return False
    return True
    