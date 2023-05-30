"""
프로그래머스 LV1: 모의고사
https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""

"""
1번: 12345
2번: 21232425
3번: 3311224455
"""

def solution(answers):
    first_method = [1, 2, 3, 4, 5]
    second_method = [2, 1, 2, 3, 2, 4, 2, 5]
    third_method = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    corrects = [0, 0, 0]
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == first_method[idx % len(first_method)]:
            corrects[0] += 1
        if answer == second_method[idx % len(second_method)]:
            corrects[1] += 1
        if answer == third_method[idx % len(third_method)]:
            corrects[2] += 1
    
    
    for idx, c in enumerate(corrects):
        if c == max(corrects):
            result.append(idx + 1)

    return result