"""
프로그래머스 LV1: 신고 결과 받기
https://school.programmers.co.kr/learn/courses/30/lessons/92334
2022 KAKAO BLIND RECRUITMENT
"""
    

def solution(id_list, report, k):
    reported = { id: 0 for id in id_list }
    report = list(set(report))
    report_count = [0] * len(id_list)
    
    for r in report:
        reporter, target_report = r.split(' ')
        reported[target_report] += 1
    
    for r in report:
        reporter, target_report = r.split(' ')
        if reported[target_report] >= k:
            report_count[id_list.index(reporter)] += 1
    
    return report_count