"""
프로그래머스 LV2: 스킬트리
https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""

def checkSkill(skill, st):
    check = True
    
    for idx, s in enumerate(st):
        if s in skill:   # 해당 스킬이 선행스킬에 포함되어 있는 경우
            required_skill = skill[0:skill.index(s)]   # 해당 스킬을 사용하기 위해 필요한 선행스킬
            before_s = st[0:idx]   # 해당 스킬 이전의 스킬들
            if all(before_s.count(rs) == 1 for rs in required_skill) == False:   # 선행스킬들 중 배우지 않은게 있으면
                check = False
                break
    return check
                
            
"""
skill: 선행 스킬 순서 (중복 없음)
skill_trees: 유저들이 만든 스킬트리
"""
def solution(skill, skill_trees):
    result = 0
    for st in skill_trees:   # 각 스킬트리 순회
        if checkSkill(skill, st) == True:   # 스킬이 사용가능한지 확인
            result += 1
    
    return result