"""
프로그래머스 LV1: 개인정보 수집 유효기간 (성공)
https://school.programmers.co.kr/learn/courses/30/lessons/150370
2023년도 KAKAO BLIND RECRUITMENT

진짜 멍청하다.. 문제 똑바로 읽자..
"""

def solution(today, terms, privacies):
    today_year, today_month, today_day = map(int, today.split('.'))
    term_dict = dict()
    result = []
    
    # term을 dict로 저장하기
    for term in terms:
        ruleType, ruleDate = term.split(' ')
        term_dict[ruleType] = int(ruleDate)
    term_type = term_dict.keys()

    for idx, privacy in enumerate(privacies):
        privacy_date, rule = privacy.split(' ')
        year, month, day = map(int, privacy_date.split('.'))
        for tt in term_type:
            if tt == rule:
                month += term_dict[tt]
                while True:
                    if month > 12:
                        year += 1
                        month -= 12
                    else:
                        break
        if today_year > year:
            result.append(idx + 1)
        elif (year == today_year) and (today_month > month):
            result.append(idx + 1)
        elif (year == today_year) and (today_month == month) and (today_day >= day):
            result.append(idx + 1)

    return result


print(solution('2022.05.19', ['A 6', 'B 12', 'C 3'], [
    '2021.05.02 A',
    '2021.07.01 B',
    '2022.02.19 C',
    '2022.02.20 C',
]))