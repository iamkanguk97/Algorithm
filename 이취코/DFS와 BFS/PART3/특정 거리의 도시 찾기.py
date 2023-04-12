# BFS와 DFS PART3 - 특정 거리의 도시 찾기
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

distance = [-1] * (N+1)
distance[X] = 0

queue = deque([X]) # 시작 노드를 먼저 queue에 넣어줌

while queue:
    temp = queue.popleft()
    
    for i in graph[temp]:
        if distance[i] == -1: # 한번도 방문안한 노드라면
            distance[i] = distance[X] + 1 # 이전 노드 거리 + 1
            queue.append(i) # 다음으로 이동한 노드 queue에 삽입

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

# 최단 거리가 K인 도시가 없으면 -> -1 출력
if check == False:
    print(-1)