"""
프로그래머스 LV1: 같은 숫자는 싫어
https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
"""

def solution(arr):
    result = []
    result.append(arr[0])   # 가장 첫번째 원소는 넣어버리기
    
    # 이후 원소들 탐색하면서 이전 원소랑 값이 다르면 배열에 추가
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    
    return result