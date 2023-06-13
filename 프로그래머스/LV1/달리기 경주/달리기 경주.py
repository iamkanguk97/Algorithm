"""
프로그래머스 LV1: 달리기 경주 (시간초과로 인한 실패)
https://school.programmers.co.kr/learn/courses/30/lessons/178871
"""

def solution(players, callings):    
    for call in callings:
        idx = players.index(call)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players