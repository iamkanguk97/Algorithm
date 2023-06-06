"""
프로그래머스 LV1: 예산
https://school.programmers.co.kr/learn/courses/30/lessons/12982
"""

def solution(d, budget):
    d = sorted(d)   # 오름차순으로 정렬
    count = 0
    
    for i in d:
        if budget < i:   # 예산보다 가격이 높을경우 중단
            break
        budget -= i   # 차감
        count += 1
    
    return count