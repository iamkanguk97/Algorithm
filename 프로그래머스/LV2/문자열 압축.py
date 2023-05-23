"""
프로그래머스 LV2: 문자열 압축
https://school.programmers.co.kr/learn/courses/30/lessons/60057

2020년도 KAKAO BLIND RECRUITMENT
"""

def solution(s):
    answer = []
    
    # s의 길이가 1이면 바로 return
    if len(s) == 1:
        return 1
    
    # 문자열 쪼갤 수 있는건 len(s) // 2 + 1
    # 문자열 길이가 8이면 최대 4개씩 자를 수 있음. 길이가 9여도 최대 4개
    for sp in range(1, (len(s)//2 + 1)):
        temp_str = s[:sp]   # 기준 문자열
        temp_result = ''
        count = 1   # 같은 문자 연속 횟수
        for i in range(sp, len(s), sp):
            target_str = s[i:i+sp]   # 비교 문자열
            if temp_str == target_str:   # 비교했는데 같을경우
                count += 1
            else:   # 비교했는데 문자열이 다른 경우
                temp_result += str(count) + temp_str if count > 1 else temp_str
                
                # 초기화 작업
                count = 1
                temp_str = s[i:i+sp]
        # 남아있는 문자열 처리
        temp_result += str(count) + temp_str if count > 1 else temp_str
        answer.append(len(temp_result))
        
    
    return min(answer)