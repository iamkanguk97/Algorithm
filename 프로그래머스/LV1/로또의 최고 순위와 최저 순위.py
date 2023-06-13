"""
프로그래머스 LV1: 로또의 최고 순위와 최저 순위
https://school.programmers.co.kr/learn/courses/30/lessons/77484
2021 Dev-Matching: 웹 백엔드 개발
"""

def getCorrectCount(lottos, win_nums):
    result = 0
    for wn in win_nums:
        if lottos.count(wn) != 0:
            result += 1
    return result

def getRank(correct):
    if correct <= 1:
        return 6
    rank = [6, 5, 4, 3, 2]
    return rank.index(correct) + 1
    

def solution(lottos, win_nums):
    correct = getCorrectCount(lottos, win_nums)   # 번호 맞춘 개수 / ex) 2이면 최소 2개번호 일치 -> 5위
    bottomRank = getRank(correct)   # 최소 순위가 될려면 그냥 그대로 냅두면 됨 (따로 작업 안함)
    
    zero_count = lottos.count(0)   # 알아보지 못할 번호 개수
    topRank = getRank(correct + zero_count)   # 최대 순위가 되려면? 나머지 0의 개수를 모두 맞추면 됨
    
    return [topRank, bottomRank]