"""
프로그래머스 LV1: 기사단원의 무기 (성공)
https://school.programmers.co.kr/learn/courses/30/lessons/136798
"""

def getDivisorCount(num):
    result = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            result.append(num//i)
            result.append(i)
    return len(set(result))
    
    
def solution(number, limit, power):
    divisors = sum([getDivisorCount(num) if getDivisorCount(num) <= limit else power for num in range(1, number+1)])
    return divisors