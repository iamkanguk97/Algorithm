"""
프로그래머스 LV1: 기사단원의 무기 (실패)
https://school.programmers.co.kr/learn/courses/30/lessons/136798
"""

def getDivisorCount(num):
    result = []
    for i in range(1, num//2+1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return len(result)
    
    

def solution(number, limit, power):
    divisors = [getDivisorCount(num) for num in range(1, number+1)]
    
    limit_over = len(list(filter(lambda x: x>limit, divisors))) * power
    limit_less = sum(list(filter(lambda x: x<=limit, divisors)))
    return limit_over + limit_less