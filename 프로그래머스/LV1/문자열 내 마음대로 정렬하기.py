"""
프로그래머스 LV1: 문자열 내 마음대로 정렬하기
https://school.programmers.co.kr/learn/courses/30/lessons/12915
"""

def solution(strings, n):
    strings = sorted(strings, key=lambda string: (string[n], string))
    return strings