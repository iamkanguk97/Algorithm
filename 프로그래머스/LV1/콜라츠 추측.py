"""
프로그래머스 LV1: 콜라츠 추측
https://school.programmers.co.kr/learn/courses/30/lessons/12943
"""

# 1이면 짝수, 2면 홀수
def check(n):
    return 1 if n % 2 == 0 else 2
    

def solution(num):
    if num == 1:   # 1이면 0 반환
        return 0
    
    count = 0
    while num != 1 and count < 500:
        checkNumber = check(num)   # 홀수인지 짝수인지 판단
        num = (num // 2) if checkNumber == 1 else (num * 3) + 1   # 1-1과 1-2
        count += 1   # 횟수 증가
    
    if count >= 500 and num != 1:   # 500회 진행했는데 1이 되지 않으면 -1반환
        return -1
    else:
        return count
        