"""
프로그래머스 LV2: 피로도
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""

from itertools import permutations

def goDungeon(dungeon, k):
    count = 0
    user_k = k
    
    for d in dungeon:   # 각 던전 순회
        if user_k >= d[0]:   # 최소 필요 피로도 만족
            user_k -= d[1]   # 소모피로도 만큼 차감
            count += 1   # 던전 입장 횟수 추가
    
    return count
    
    
    
def solution(k, dungeons):
    dungeons = permutations(dungeons, len(dungeons))   # 던전 배열을 순열로 만든다
    temp = []
    
    for dungeon in dungeons:   # 각 순열 원소를 순회하면서
        result = goDungeon(dungeon, k)   # 각 순열 탐색 시작
        temp.append(result)
    
    return max(temp)   # 순열 리스트 중에서 최대 던전수 return