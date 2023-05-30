"""
프로그래머스 LV1: 최소직사각형
https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""

def solution(sizes):
    answer = 0
    row = []
    col = []

    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
        row.append(s[0])
        col.append(s[1])

    return max(row) * max(col)