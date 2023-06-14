"""
프로그래머스 LV1: 바탕화면 정리
https://school.programmers.co.kr/learn/courses/30/lessons/161990
"""

"""
. . . . . . . . . .
. . . . . # . . . .
. . . . . . # # . .
. . . # # . . . . .
. . . . # . . . . .
"""

def solution(wallpaper):
    # print(wallpaper)
    
    topIdx, leftIdx, rightIdx, bottomIdx = None, None, None, None

    # (1) 위부터 몇번째 줄에 처음으로 #이 나오는지 확인
    for idx, wall in enumerate(wallpaper):
        if wall.count('#') >= 1:
            topIdx = idx
            break
            
    # (2) 왼쪽부터 몇번째 줄에 처음으로 #이 나오는지 확인
    for i in range(len(wallpaper[0])):
        find = False
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == '#':
                leftIdx = i
                find = True
                break
        if find == True:
            break
    
    # (3) 밑에부터 몇번째 줄에 처음으로 #이 나오는지 확인
    for idx, wall in reversed(list(enumerate(wallpaper))):
        if wall.count('#') >= 1:
            bottomIdx = idx
            break
    
    # (4) 오른쪽부터 몇번째 줄에 처음으로 #이 나오는지 확인
    for i in range(len(wallpaper[0])-1, -1, -1):
        find = False
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == '#':
                rightIdx = i
                find = True
                break
        if find == True:
            break
    
    # print(leftIdx, rightIdx, topIdx, bottomIdx)
    
    return [topIdx, leftIdx, bottomIdx + 1, rightIdx + 1]