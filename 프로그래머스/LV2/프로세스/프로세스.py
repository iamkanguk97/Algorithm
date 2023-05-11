"""
프로그래머스 LV2: 프로세스
https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""

from collections import deque

def solution(priorities, location):
    temp = [(i, priorities[i]) for i in range(len(priorities))]
    queue = deque(temp)   # queue로 선언
    answer = 0
    
    while queue:
        data = queue.popleft()   # queue에서 data를 꺼냄
        bigCheck = False
        for i in range(len(queue)):
            if data[1] < queue[i][1]:   # pop 했을 때 우선순위가 더 높은게 있다면
                bigCheck = True
                queue.append(data)   # 다시 queue에 insert
                break
        if bigCheck == False:   # 우선순위가 더 큰 프로세스가 없다면 꺼낸 프로세스 실행
            answer += 1
            if data[0] == location:   # 찾는 location과 일치하는 경우 반복문 탈출 + 횟수 return
                break
    
    return answer


priorities = [2, 1, 3, 2]
print(solution(priorities, 2))