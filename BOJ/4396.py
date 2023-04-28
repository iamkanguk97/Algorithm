"""
백준 4396번: 지뢰 찾기
https://www.acmicpc.net/problem/4396
"""

N = int(input())  # N개의 줄
mine = [list(input().rstrip()) for _ in range(N)]   # 지뢰의 위치
table = [list(input().rstrip()) for _ in range(N)]   # 열린칸에는 주변에 지뢰가 몇개있는지
findMine = False   # 마인을 확인했는지에 대한 변수

def mine_count(mine, x, y):
    # 상하좌우 + 북서/북동/남서/남동
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    count = 0
    for i in range(8):
        # x,y좌표 이동
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        else:
            if mine[nx][ny] == '*':
                count += 1

    return count


for i in range(N):
    for j in range(N):
        if table[i][j] == 'x':   # 해당 칸이 열려있는 상태
            if mine[i][j] == '*':   # 그 칸에 지뢰가 있음
                findMine = True   # 열려있는 상태에서 마인 찾았다고 표시
                continue

            mc = mine_count(mine, i, j)
            table[i][j] = str(mc)
            


# 열린 상태에서 지뢰를 본적이 있음 -> mine을 순회하면서 지뢰인 부분의 좌표를 기억해서 table에 기록
if findMine == True:
    for a in range(N):
        for b in range(N):
            if mine[a][b] == '*':
                table[a][b] = '*'

# 출력하는 부분
for r in range(N):
    print(''.join(table[r]))