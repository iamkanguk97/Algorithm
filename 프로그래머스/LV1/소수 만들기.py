"""
프로그래머스 LV1: 소수 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12977
Summer/Winter Coding(~2018)
"""

from itertools import combinations

def isNumeric(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    comb = [sum(i) for i in list(combinations(nums, 3))]
    result = len(list(filter(lambda x: isNumeric(x) == True, comb)))
    return result