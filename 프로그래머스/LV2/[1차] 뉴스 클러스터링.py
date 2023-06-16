"""
프로그래머스 LV2: 뉴스 클러스터링
https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""

import re

def getSubset(temp):
    # temp = temp.replace(' ', '')   # 공백 없앰
    # temp = re.sub(r"[^a-zA-Z]", "", temp).upper()   # 숫자, 특수문자 없앰
    temp_set = []
    for i in range(1, len(temp)):   # 부분집합 추출
        if temp[i-1].isalpha() and temp[i].isalpha():
            temp_set.append(temp[i-1:i+1].upper())
    
    return temp_set
    
    
def solution(str1, str2):
    substr1, substr2 = getSubset(str1), getSubset(str2)
    
    # 교집합과 합집합의 개수를 구함
    jrate = None
    ts = list(set(substr1 + substr2))
    # print(ts)
    
    if len(ts) == 0:
        jrate = 1
    else:
        substr1_count, substr2_count = [0] * len(ts), [0] * len(ts)
        inter, union = 0, 0
        for i in range(len(substr1)):
            find = ts.index(substr1[i])
            substr1_count[find] += 1
        for i in range(len(substr2)):
            find = ts.index(substr2[i])
            substr2_count[find] += 1
        
        for k in range(len(ts)):
            inter += min(substr1_count[k], substr2_count[k])
            union += max(substr1_count[k], substr2_count[k])
        
        jrate = inter / union
    
    # print(jrate)
    return int(jrate * 65536)