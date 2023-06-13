"""
프로그래머스 LV1: K번째수
https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""

def solution(array, commands):
    result = []
    
    for c in commands:
        i, j, k = c
        sliced = sorted(array[i-1:j])
        result.append(sliced[k-1])
    
    return result