"""
프로그래머스 LV1: 정수 제곱근 판별
https://school.programmers.co.kr/learn/courses/30/lessons/12934
"""

import math

def solution(n):
    base = int(math.sqrt(n))
    if base ** 2 == n:
        return (base+1) ** 2
    else:
        return -1