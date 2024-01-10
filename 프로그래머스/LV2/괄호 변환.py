def isRight(p):   # 문자열 p가 올바른 괄호 문자열인지 확인하는 함수
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False

def splitToUAndV(p):   # 문자열 p를 u와 v로 분리 (u는 균형잡힌 괄호 문자열, v는 나머지)
    openBracketCount, closeBracketCount = 0, 0
    for idx, w in enumerate(p):
        if w == '(':
            openBracketCount += 1
        else:
            closeBracketCount += 1
        if openBracketCount == closeBracketCount:
            return p[:idx+1], p[idx+1:]

def solution(p):
    if not p:   # 1. 빈 문자열인 경우 그대로 빈 문자열 반환
        return p
    
    u, v = splitToUAndV(p)   # 2. 문자열을 u와 v로 분리
    
    if isRight(u) == True:   # 3. 문자열이 올바른 괄호 문자열이라면
        return u + solution(v)   # 3-1. v에 대해 1단계부터 다시 수행
    else:   # 4. 문자열 u가 올바른 괄호 문자열이 아닌 경우
        answer = '('   # 4-1. (를 붙임
        answer += solution(v)   # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 붙임
        answer += ')'   # 4-3. )를 붙임
        
        for i in u[1:len(u)-1]:   # 4-4. u의 첫번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향 뒤집음
            if i == '(':
                answer += ')'
            else:
                answer += '('    
    return answer   # 4-5. 반환
    
    