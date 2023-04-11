# DFS와 BFS PART2 실전문제) 음료수 얼려먹기

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x, y):
    # 좌표가 범위 벗어나면 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    # 현재 노드를 방문하지 않음
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리

        # 상하좌우 모두 재귀적으로 DFS 함수 호출
        dfs(x+1, y) 
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)