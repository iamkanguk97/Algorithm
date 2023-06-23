"""
프로그래머스 LV2: 이모티콘 할인행사
https://school.programmers.co.kr/learn/courses/30/lessons/150368
2023년도 KAKAO BLIND RECRUITMENT
"""

from itertools import product

def solution(users, emoticons):
    answer = [0, 0]   # 플러스 가입 수, 이모티콘 매출액
    discounts = [10, 20, 30, 40]   # 할인율 종류 (10% ~ 40%)
    for discount in product(discounts, repeat=len(emoticons)):   # 각 이모티콘에 할당되는 할인율 조합들
        total_pay, plus_sign = 0, 0
        for rate, price in users:   # 각 유저들 순회
            pay = 0
            for idx, emoticon_price in enumerate(emoticons):
                if discount[idx] >= rate:
                    pay += int(emoticon_price * (100 - discount[idx]) / 100)
            if pay >= price:   # 구매한 이모티콘 총 비용이 각 유저에 할당되어 있는 결제 금액보다 큰 경우 플러스 가입 가능
                plus_sign += 1
            else:   # 플러스 가입 못하는 경우
                total_pay += pay
        if plus_sign > answer[0]:   # 이모티콘 플러스 가입자 수가 증가한 경우
            answer[0], answer[1] = plus_sign, total_pay
        elif plus_sign == answer[0] and total_pay > answer[1]:
            answer[1] = total_pay
    
    return answer