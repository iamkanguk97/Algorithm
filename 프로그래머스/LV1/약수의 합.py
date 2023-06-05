"""
프로그래머스 LV1: 약수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/12928
"""

"""
ex) n = 12이면 1,2,3,4,6,12임
range(1, 12+1)까지 할 필요가 없음.
자기 자신은 항상 포함이 되기 때문에 제외하고 해도됨.
"""

def solution(n):
    return n + sum([num for num in range(1, n//2+1) if n % num == 0])