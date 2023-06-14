"""
프로그래머스 LV1: 개인정보 수집 유효기간 (실패)
https://school.programmers.co.kr/learn/courses/30/lessons/150370
2023년도 KAKAO BLIND RECRUITMENT
"""

def addDate(date, num):
    # 예를 들어 유효기간이 2달이고 2022.04.07이면 2022.06.06까지 유효
    year, month, day = map(int, date.split('.'))   # [2022, 04, 07]
    # month += int(num)   # 해당 유효기간만큼 월에서 더해줌
    # if month >= 13:
    #     year += month // 12
    #     month = month % 12
    for _ in range(int(num)):
        month += 1
        if month == 13:
            year += 1
            month = 1
        
    day -= 1
    if day == 0:
        day = 28
        month -= 1
        if month == 0:
            year -= 1
    
    # return되는 날까지 유효한 거임!
    return [year, month, day]
    
    
def isInvalid(date1, date2):
    # date1: 유효기간 만료 날짜, date2: 오늘 날짜
    if date1[0] < date2[0]:
        return True
    else:
        if date1[1] < date2[1]:
            return True
        else:
            if date1[2] <= date2[2]:
                return True
    
    return False

def solution(today, terms, privacies):
    # today -> 오늘
    # term -> 각 약관이 유효기간이 얼마나 되는지 (유효기간은 1달~20달)
    # privacies -> 각 개인정보 수집 일자가 언제고 약관종류가 무엇인지
    
    result = []
    for idx, privacy in enumerate(privacies):
        get_date, rule = privacy.split(' ')   # 개인정보 수집 일자, 약관 종류
        for term in terms:
            rule_type, rule_date = term.split(' ')   # 약관 종류, 유효 기간
            if rule == rule_type:   # 약관 종류를 찾으면
                addedDate = addDate(get_date, rule_date)   # 유효기간만큼 날짜에서 더해주기
                print(addedDate)
                if isInvalid(addedDate, list(map(int, today.split('.')))) == True:   # 유효기간을 넘으면 파기처리
                    result.append(idx + 1)
                break
                
                
    return sorted(result)