"""
프로그래머스 LV1: 두 개 뽑아서 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/68644
"""

from itertools import combinations

def solution(numbers):
    data = sorted(list(map(lambda x: sum(x), list(combinations(numbers, 2)))))
    data = sorted(list(set(data)))
    return data