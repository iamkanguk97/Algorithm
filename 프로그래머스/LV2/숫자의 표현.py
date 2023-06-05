"""
프로그래머스 LV2: 숫자의 표현
https://school.programmers.co.kr/learn/courses/30/lessons/12924
"""

def solution(n):
    count = 1   # 자기 자신만 더하는건 무조건 가능하기 때문에 미리 1
    for i in range(1, (n//2) + 1):    # 해당 숫자의 반까지만 확인해도 가능
        temp_i = i
        data = 0   # 계산 값
        while True:
            data += temp_i
            if data >= n:   # 해당 숫자를 넘었을 경우
                if data == n:   # 해당 숫자랑 값이 동일한 경우에는 count 추가
                    count += 1
                break
            temp_i += 1
    return count
        