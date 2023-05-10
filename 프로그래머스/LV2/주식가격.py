"""
프로그래머스 LV2: 주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584
"""

def solution(prices):
    answer = []
    
    # 1초부터 (prices의 길이)초만큼 반복문 순회
    for sec in range(1, len(prices)+1):
        decreaseCheck = False   # 감소하는 값 확인했는지 체크하는 변수
        for i in range(sec, len(prices)):
            if prices[sec-1] > prices[i]:   # 해당 시점의 가격보다 낮은 가격이 있다면 (떨어지고 있는 시점을 확인)
                decreaseCheck = True   # 감소하는 값 확인 표시
                answer.append(i+1-sec)   # 가격이 떨어지지 않은 시간 append
                break   # 반복문 탈출
        if decreaseCheck == False:   # 해당 시점의 가격보다 낮은 가격이 없음
            answer.append(len(prices) - sec)   # 가격이 떨어지지 않은 기간을 append
    
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))