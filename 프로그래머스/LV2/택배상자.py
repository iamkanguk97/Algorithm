"""
프로그래머스 LV2: 택배상자
https://school.programmers.co.kr/learn/courses/30/lessons/131704
"""

"""
<문제해석>
---4321 -> (영재)
하지만 받아서 바로 트럭에 넣으면 기사님이 배달하는 순서랑 섞어서 문제생김

트럭에 실어야 하는 순서가 아니면 그 상자를 다른 곳에 보관해야함 (보조 컨테이너 벨트)
보조 컨테이너 벨트: 가장 마지막에 넣은 상자부터 꺼냄 (스택)

보조 컨테이너 벨트 사용해도 기사님이 원하는대로 상자를 못실으면 상자를 싣지 않는다.
"""

def solution(order):
    box = 1
    sub_belt = []   # 보조 벨트
    
    count = 0
    for idx, od in enumerate(order):
        if sub_belt.count(od) == 0:   # 보조벨트에 기사님이 원하는 박스가 없는 경우
            while box != od:   # 기사님이 원하는 박스가 나올때까지 메인벨트의 박스를 보조벨트로 옮김
                sub_belt.append(box)
                box += 1
            count += 1   # 기사님께 전달
            box += 1   # 메인벨트에서 다음박스 꺼냄
        else:
            subPopBox = sub_belt[-1]
            if subPopBox != od:   # 서브벨트에서 꺼내지 못하는 경우 프로그램 종료
                break
            sub_belt.pop()   # 보조벨트에서 기사님이 원하는 상자 꺼냄
            count += 1
            
    return count