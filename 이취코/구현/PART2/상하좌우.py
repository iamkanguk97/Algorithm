"""
이취코 구현 PART2: 상하좌우
난이도: 1
"""

n = int(input())   # 공간의 크기   
movePlan = list(map(str, input().split()))   # 이동계획
x, y = 1, 1   # 시작 좌표

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = ['U', 'D', 'L', 'R']

for mp in movePlan:
    dIdx = direction.index(mp)   # direction index
    
    # 좌표 이동
    nx = x + dx[dIdx]
    ny = y + dy[dIdx]

    if nx < 1 or nx > n or ny < 1 or ny > n:   # 공간 밖을 넘어가면 스킵
        continue
    else:
        x, y = nx, ny


print(x, y)