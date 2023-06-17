"""
프로그래머스 LV2: 주차 요금 계산
https://school.programmers.co.kr/learn/courses/30/lessons/92341
2022년도 KAKAO BLIND RECRUITMENT
"""

"""
feeds: [기본시간, 기본요금, 단위시간, 단위요금]
records: [입차시간, 차량번호, in/out]
"""

import math

def solution(fees, records):
    # 입차-출자 집합으로 모음, 출차 기록이 없으면 출차를 23:59분으로 세팅
    temp = {}
    totalTime = {}
    
    for record in records:
        enter_time, car_number, option = record.split(' ')
        h, m = map(int, enter_time.split(':'))
        if option == 'IN':   # 입차
            temp[car_number] = h * 60 + m   # temp에 입차시간 기록 (분)
        else:   # 출차
            parking = abs(temp[car_number] - (h * 60 + m))
            if car_number in totalTime:   # 한번 입차-출차 기록이 있으면
                totalTime[car_number] += parking   # 누적시간 더해줌
            else:   # 입차-출차 기록이 없으면
                totalTime[car_number] = parking   # 입차시간에서 출차시간 빼서 total에 넣음
                
            temp.pop(car_number)   # temp에서 삭제
        
    # 입차하고 출차한 기록이 없는 차량들 조회
    for k, v in temp.items():
        parking = abs(v - (23 * 60 + 59)) 
        if k in totalTime:
            totalTime[k] += parking
        else:
            totalTime[k] = parking
    
    totalTime = sorted(totalTime.items())   # 차량 번호 순으로 정렬
    result = []
    for data in totalTime:
        ptime = data[1]
        if fees[0] >= ptime:   # 기본시간을 넘지 않은 경우
            result.append(fees[1])   # 기본 요금만 넣음
        else:   # 기본시간을 넘으면 요금 계산
            result.append(fees[1] + fees[3] * math.ceil((ptime - fees[0]) / fees[2]))
    
    return result