"""
백준 2578번: 빙고
https://www.acmicpc.net/problem/2578
"""
import sys
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(5)]   # 빙고판
try_bingo = [list(map(int, input().split())) for _ in range(5)]   # 사회자가 부르는 수
result = 0
idx = 0
bingoCount = 0

# 빙고판에 해당 번호가 있는지 확인하고 x,y 좌표에 해당하는 부분 X처리
def find_number(matrix, value):
    dx, dy = 0, 0

    for a in range(5):
        for b in range(5):
            if matrix[a][b] == value:
                matrix[a][b] = 0
                dx = a
                dy = b
                break

    return dx, dy


def check_bingo(matrix, x, y):
    bgCount = 0
    crossCheckResult = False

    rowCheckResult = row_check(matrix, x)   # 가로 확인
    colCheckResult = col_check(matrix, y)   # 세로 확인

    # x=y이거나 x+y가 4이면 대각선 확인
    if x == y:
        crossCheckResult = cross_check(matrix, 'equal')
    elif x + y == 4:
        crossCheckResult = cross_check(matrix, 'plus')

    if rowCheckResult == True:
        bgCount += 1
    if colCheckResult == True:
        bgCount += 1
    if crossCheckResult == True:
        bgCount += 1

    return bgCount

def row_check(matrix, x):
    checkRowBingo = True
    for i in range(5):
        if matrix[x][i] != 0:
            checkRowBingo = False
            break
    
    return checkRowBingo
        

def col_check(matrix, y):
    checkColBingo = True
    for i in range(5):
        if matrix[i][y] != 0:
            checkColBingo = False
            break

    return checkColBingo

def cross_check(matrix, option):
    checkCrossBingo = True
    
    if option == 'equal':
        for i in range(5):
            if matrix[i][i] != 0:
                checkCrossBingo = False
    elif option == 'plus':
        for i in range(5):
            if matrix[i][4-i] != 0:
                checkCrossBingo = False
    
    return checkCrossBingo


for i in range(5):
    for j in range(5):
        idx += 1
        dx, dy = find_number(matrix, try_bingo[i][j])   # O처리 진행
        
        if idx >= 5:   # 빙고 시작한지 5턴 이상이면
            bingoCount += check_bingo(matrix, dx, dy)
            if bingoCount >= 3:
                result = idx
                break
    if bingoCount >= 3:
        break

print(result)