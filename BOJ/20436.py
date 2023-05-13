"""
백준 20436 (S4): ZOAC 3
https://www.acmicpc.net/problem/20436
"""

def findPos(w):
    for i in range(len(keyboard)):
        if w in keyboard[i]:
            return i, keyboard[i].index(w)


# 거리 계산 함수
def calDistance(lx, ly, rx, ry):
    return abs(lx - rx) + abs(ly - ry)

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']   # 키보드 키
moum = 'byhnujmikolp'   # 모음

sl, sr = map(str, input().split())   # 두 알파벳 소문자 sl, sr 입력
word = input()   # 문자열 입력 받음
total_time = 0

lx, ly = findPos(sl)   # 왼쪽 손가락 좌표
rx, ry = findPos(sr)   # 오른쪽 손가락 좌표

for w in word:
    wx, wy = findPos(w)   # 해당 글자 좌표 가져오기
    tx, ty = None, None   # 손가락 임시 좌표
    temp_time = 0

    if w in moum:   # 모음 -> 오른쪽 손가락
        dis = calDistance(rx, ry, wx, wy)   # 거리계산
        if dis != 0:   # 거리가 0이 아니면 거리시간 추가
            temp_time += dis
            rx, ry = wx, wy   # 좌표 이동
        temp_time += 1   # 타자치는시간 추가
    else:   # 자음 -> 왼쪽 손가락
        dis = calDistance(lx, ly, wx, wy)   # 거리계산
        if dis != 0:   # 거리가 0이 아니면 거리시간 추가
            temp_time += dis
            lx, ly = wx, wy   # 좌표 이동
        temp_time += 1   # 타자치는시간 추가
    
    total_time += temp_time

print(total_time)