"""
이취코 DFS/BFS PART2: 음료수 얼려먹기
난이도: 1.5 / 3
"""

n, m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:   # 좌표 넘어가면 함수 종료
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False



count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)