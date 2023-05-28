"""
프로그래머스 LV2: 기능개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
"""

from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque([[progresses[i], speeds[i]] for i in range(len(progresses))])   # Queue 생성
    
    while queue:   # Queue가 빌때까지
        # 개발 진행
        for _ in range(len(queue)):
            project = queue.popleft()
            if project[0] < 100:   # 진행률이 100미만이면 진행률만큼 증가
                project[0] += project[1]
            queue.append(project)   # 다시 queue에다 넣어줌
        
        # 다음날 넘어가기 전 배포할 수 있는게 있는지 확인
        production = 0   # 배포한 기능 개수
        while queue:
            data = queue.popleft()   # 맨 위의 작업을 뺌
            if data[0] >= 100:   # 진행률이 100 (100이상)이면 배포진행
                production += 1
            else:   # 진행률이 100 미만인게 있으면 다음날로 넘어가야함
                queue.appendleft(data)   # 다시 원래 자리에 작업넣음
                break   # 배포단계 중단
        
        if production != 0:   # 배포한 기능이 있으면 결과배열에 넣음
            answer.append(production)
    
    return answer