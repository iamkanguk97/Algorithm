"""
프로그래머스 LV1: 부족한 금액 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/82612
"""

def solution(price, money, count):
    totalPrice = sum([num for num in range(price, price*count+1, price)])
    return totalPrice - money if totalPrice > money else 0