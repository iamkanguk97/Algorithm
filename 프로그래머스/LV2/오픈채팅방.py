"""
프로그래머스 LV2: 오픈채팅방
https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=python3
2019년도 KAKAO BLIND RECRUITMENT
"""

# [Enter/Leave/Change, 유저아이디, 닉네임]
# 무지 들어옴 -> 프로도 들어옴 -> 무지 나감 -> 프로도 들어옴 -> Ryan

def solution(record):
    info = {}
    
    result = []
    for rec in record:
        rec_split = rec.split(' ')
        
        if rec_split[0] == 'Enter':   # 입장
            user_id = rec_split[1]
            nickname = rec_split[2]
            
            result.append(user_id + '님이 들어왔습니다.')
            info[user_id] = nickname   # 입장할 때 닉네임 변경 가능성이 있기 때문에 사전 업데이트
        elif rec_split[0] == 'Leave':
            result.append(rec_split[1] + '님이 나갔습니다.')
        else:
            info[rec_split[1]] = rec_split[2]   # 닉네임 변경으로 인한 업데이트
    
    for idx, r in enumerate(result):
        userId = r[:r.index('님')]
        new_r = r.replace(userId, info[userId])
        result[idx] = new_r
        
    return result