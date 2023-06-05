"""
프로그래머스 LV1: 가운데 글자 가져오기
https://school.programmers.co.kr/learn/courses/30/lessons/12903
"""

def solution(s):
    if len(s) <= 2:
        return s
    else:
        checkNum = len(s) % 2   # 홀수인지 짝수인지
        temp = len(s) // 2   # 길이에서 반 나눈값
        if checkNum == 1:
            return s[temp]
        else:
            return s[temp-1] + s[temp]