"""
프로그래머스 LV1: 햄버거 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/133502
"""

def solution(ingredient):
    # 1: 빵, 2: 야채, 3: 고기
    # [1,2,3,1]
    burger = []
    made = [1, 2, 3, 1]
    
    result = 0
    for ing in ingredient:
        burger.append(ing)
        if ing == 1 and len(burger) >= 4:   # 재료가 빵이고 최소 4개의 재료가 들어가있을때
            # burger stack에 1231순으로 들어가있는지 확인
            ing_count = len(burger)
            check = burger[ing_count-4:ing_count+1]
            if check == made:   # 햄버거 만들 수 있음
                del burger[ing_count-4:ing_count+1]
                result += 1
    
    return result