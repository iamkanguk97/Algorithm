"""
프로그래머스 LV2: 피보나치 수
https://school.programmers.co.kr/learn/courses/30/lessons/12945

재귀함수로 호출하면 시간초과 에러 발생
따라서 재귀함수 사용하지 않고 for문 사용
"""

def fibo(num):
    answer = [0, 1]
    for i in range(2, num+1):
        answer.append((answer[i-2] + answer[i-1]) % 1234567)
    return answer[-1]
        
    
def solution(n):
    return fibo(n)