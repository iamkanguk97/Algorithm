"""
프로그래머스 LV2: k진수에서 소수 개수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/92335
2022년도 KAKAO BLIND RECRUITMENT
"""

import math

def convert(n, base):
    temp = '0123456789ABCDEF'
    q, r = divmod(n, base)
    return convert(q, base) + temp[r] if q else temp[r]

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def check(data):
    splited = data.split('0')
    count = 0
    for sd in splited:
        if sd == '':
            continue
        if isPrime(int(sd)) == True:
            count += 1
    
    return count

def solution(n, k):
    convert_n = convert(n, k)   # k진법으로 바꾼 이후
    return check(convert_n)