"""
프로그래머스 LV1: [1차] 다트 게임
https://school.programmers.co.kr/learn/courses/30/lessons/17682
2018년도 KAKAO BLIND RECRUITMENT
"""

import math

# 문자열 자르기
def splitDart(dartResult):
    result = []
    idx, curr = 0, 0
    while idx < len(dartResult):
        if dartResult[idx].isalpha():
            temp = None
            # 뒤에 특수문자가 있는지 확인
            if idx + 1 <= len(dartResult)-1 and dartResult[idx + 1] in '*#':
                temp = (int(dartResult[curr:idx]), dartResult[idx], dartResult[idx+1])
                idx += 2
                curr = idx
            else:
                temp = (int(dartResult[curr:idx]), dartResult[idx], None)
                idx += 1
            result.append(temp)
            curr = idx
        else:
            idx += 1
    
    return result

def bonusNumber(bonus):
    if bonus == 'S':
        return 1
    elif bonus == 'D':
        return 2
    else:
        return 3
            

def solution(dartResult):
    dart_split = splitDart(dartResult)   # dartResult를 리스트로 나누기 / ex) 1D 2S# 10S => ['1D', '2S#', '10S']
    result = []
    
    for idx, dart in enumerate(dart_split):
        score, bonus, option = dart
        
        new_score = int(math.pow(score, bonusNumber(bonus)))
        result.append(new_score)
        
        if option != None:
            if option == '*':   # 스타상: 해당 점수와 바로 전에 얻은 점수를 각 2배
                if idx != 0:
                    result[idx-1] *= 2
                result[idx] *= 2
            else:   # 아차상: 해당 점수 마이너스
                result[idx] *= -1
                
    return sum(result)
                
        
            
        
    