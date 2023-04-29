"""
백준 2578번: 빙고
https://www.acmicpc.net/problem/2578

이전에 작업한 코드랑 진짜 로직은 완전 똑같은데.... 왜 틀린지는 잘 모르겠지만
해당 코드는 깔끔하고 배울 부분이 많은거 같아서 참고했다.
"""

def isBingo(arr):
    bgCount = 0

    # (1) 가로 줄 확인
    for row in arr:
        if row.count(0) == 5:   # 해당 행에서 0의 개수가 5개 -> 맞은거임
            bgCount += 1 

    # (2) 세로 줄 확인
    for i in range(5):
        tmp = 0
        for j in range(5):
            if arr[j][i] == 0:
                tmp += 1
        if tmp == 5:
            bgCount += 1

    # (3) 왼쪽->오른쪽 대각선 확인
    tmp2 = 0
    for i in range(5):
        if arr[i][i] == 0:
            tmp2 += 1
    if tmp2 == 5:
        bgCount += 1

    # (4) 오른쪽->왼쪽 대각선 확인
    tmp3 = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            tmp3 += 1
    if tmp3 == 5:
        bgCount += 1

    return bgCount


bingo = [list(map(int, input().split())) for _ in range(5)]   # 빙고판
tutor = []   # 하나씩 부를 숫자

# 사회자가 하나씩 부르는 숫자 1차원 배열로 세팅
for _ in range(5):
    tutor_temp = list(map(int, input().split()))
    for tt in tutor_temp:
        tutor.append(tt)

for idx, num in enumerate(tutor):
    for bg in bingo:   # 빙고판에서 1번째줄부터 확인
        if num in bg:   # 해당 줄에 사회자가 부른 번호가 포함되어 있으면
            bg[bg.index(num)] = 0   # 해당 부분 0으로 UPDATE
            break
    bingoCount = isBingo(bingo)   # 맞은 줄 개수 확인
    if bingoCount >= 3:
        print(idx + 1)
        exit()