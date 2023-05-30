"""
프로그래머스 LV2: 소수찾기
https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""

from itertools import permutations

# 소수 판별 함수
def isPrime(num):
    if num <= 1:
        return False
    
    for n in range(2, num):
        if num % n == 0:
            return False
    
    return True


def solution(numbers):
    pset = set()
    answer = 0
    
    for i in range(1, len(numbers)+1):
        perm = permutations(numbers, i)   # 순열 생성
        for p in perm:
            pdata = "".join(map(str, p))    # 순열 데이터들
            pset.add(pdata)
            
    pset = set(map(int, pset))    # 중복제거
    for num in pset:
        if isPrime(num) == True:   # 소수면 1 추가
            answer += 1
    
    return answer