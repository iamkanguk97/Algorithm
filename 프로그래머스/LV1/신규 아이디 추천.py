"""
프로그래머스 LV1: 신규 아이디 추천
https://school.programmers.co.kr/learn/courses/30/lessons/72410
"""

def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for word in new_id:
        if word.islower() or word.isdigit() or word in ['-', '_', '.']:
            answer += word
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
            
    # 5단계
    if len(answer) == 0:
        answer = 'a'
        
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer