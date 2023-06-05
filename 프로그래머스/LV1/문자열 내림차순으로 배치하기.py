"""
프로그래머스 LV1: 문자열 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12917
"""

def solution(s):
    return "".join(sorted(s, reverse=True))