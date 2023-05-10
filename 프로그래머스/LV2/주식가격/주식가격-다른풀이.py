from collections import deque

def solution(prices):
    queue = deque(prices)   # queue로 지정
    result = []
    
    while queue:   # queue에 data가 있는동안
        price = queue.popleft()   # 시간 순서대로의 price를 pop한다
        time = 0   # 시간 변수

        for p in queue:   # 첫 가격 빼고 남은 데이터들 반복문 순회
            time += 1   # 시간 1 추가
            if price > p:   # 감소세가 보이면
               break 
        result.append(time)

    return result

prices = [1, 2, 3, 2, 3]
print(solution(prices))