"""
프로그래머스 LV1: 숫자 짝궁 (11~16번 테스트케이스 시간 초과로 실패)
https://school.programmers.co.kr/learn/courses/30/lessons/131128
"""

def solution(X, Y):
    x_dict = { x: X.count(x) for x in set(X)}
    y_dict = { y: Y.count(y) for y in set(Y)}
    
    data = []
    for x_key, x_value in x_dict.items():
        if x_key in y_dict.keys():
            for _ in range(min(x_dict[x_key], y_dict[x_key])):
                data.append(x_key)
    
    if len(data) == 0:
        return '-1'
    else:
        data = sorted(data, reverse=True)
        data = int("".join(data))
        return str(data)