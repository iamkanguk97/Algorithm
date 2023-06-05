"""
프로그래머스 LV1: 나머지가 1이 되는 수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/87389
"""

"""
n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수?
ex) n = 10이야 3으로 나눈게 가장 작음
일단 x는 10보다 작아야함
"""

def solution(n):
    answer = 0
    
    for x in range(2, n):
        answer = n % x
        if answer == 1:
            answer = x
            break
    
    return answer