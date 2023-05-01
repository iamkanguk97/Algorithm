"""
백준 1244번: 스위치 켜고 끄기
https://www.acmicpc.net/problem/1244
"""

switch_count = int(input())   # 스위치 개수
switch_status = [-1] + list(map(int, input().split()))   # 각 스위치 상태 (켜져있으면 1, 꺼져있으면 0)
student_count = int(input())   # 학생 수

def update_status(switch_status, idx):
    if switch_status[idx] == 1:
        switch_status[idx] = 0
    else:
        switch_status[idx] = 1
    return

for _ in range(student_count):
    gender, snum = map(int, input().split())
    
    if gender == 1:   # 남자
        for i in range(snum, switch_count+1, snum):   # 학생 번호의 배수는 번호 업데이트 처리
            update_status(switch_status, i)
    else:   # 여자
        for i in range(switch_count // 2):
            if snum - i < 1 or snum + i > switch_count:
                break
                
            if switch_status[snum - i] == switch_status[snum + i]:   # 좌우가 같으면 상태 변경
                update_status(switch_status, snum - i)
                update_status(switch_status, snum + i)
            else:
                break
        update_status(switch_status, snum)   # 원래 포지션 상태 변경


for i in range(1, switch_count+1):
    print(switch_status[i], end = " ")
    if i % 20 == 0:
        print()