"""
프로그래머스 LV2: 다음 큰 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12911
"""

# 2진수로 변환해주는 함수
# 알고보니 파이썬에 bin 메서드가 있었음 ㅎ
def makeBin(num):
    result = ''
    while num >= 1:
        m, r = num // 2, num % 2
        result += str(r)
        num = m
    return result[::-1]
    

def solution(n):
    bin = makeBin(n)   # 2진수로 변환
    one_count = bin.count('1')   # 1 개수 세기
    
    while True:
        n += 1   # 1씩 증가해서 확인함 (완탐?)
        temp_bin = makeBin(n)   # 증가한 숫자 2진수로 변환
        if one_count == temp_bin.count('1'):   # 1 개수 비교
            return n