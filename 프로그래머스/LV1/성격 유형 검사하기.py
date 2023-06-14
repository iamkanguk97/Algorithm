"""
프로그래머스 LV1: 성격 유형 검사하기
https://school.programmers.co.kr/learn/courses/30/lessons/118666
2022년도 KAKAO TECH INTERNSHIP
"""

"""
RT: R은 1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형
    T는 1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형

예를 들어.. AN CF 등이라고 하면
AN: 4번지표 (1번 질문에서 비동의를 하면 A, 동의를 하면 N) (어피치형 3-2-1, 모르겠음, 네오형 1-2-3)
CF: 2번지표 (2번 질문에서 비동의를 하면 C, 동의를 하면 F) (콘형 3-2-1, 모르겠음 프로도형 1-2-3)
"""

def solution(survey, choices):
    result = ''
    score = [0, 3, 2, 1, 0, 1, 2, 3]   # 1부터 7까지의 choices (1~3: 비동의, 4: 모르겠음, 5~7: 동의)
    score_point = [{ 'R': 0, 'T': 0}, { 'C': 0, 'F': 0}, { 'J': 0, 'M': 0 }, { 'A': 0, 'N': 0 }]
    
    for i in range(len(survey)):
        choice = choices[i]
        if choice == 4:   # Choice가 4면 선택안함 -> 무시
            continue
        else:
            for sp in score_point:
                survey_temp = survey[i][1] if choice >= 5 else survey[i][0]
                if list(sp.keys()).count(survey_temp) == 1:
                    sp[survey_temp] += score[choice]
                    break
    
    for sp in score_point:
        sorted_sp = sorted(sp.items(), key=lambda x: (-x[1], x[0]))
        result += sorted_sp[0][0]
        
    return result