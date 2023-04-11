# BFS 기본 코드 (너비 우선 탐색)
from collections import deque

def bfs(graph, start, visited):
    # BFS에서는 Queue를 사용하기 때문에 deque 라이브러리 사용
    queue = deque([start]) # start 노드를 queue에 넣음

    # 시작 노드를 방문처리
    visited[start] = True

    # Queue에 data가 없을때까지 진행
    while queue:
        v = queue.popleft() # Queue에서 노드를 꺼냄
        print(v, end=' ')

        for i in graph[v]: # 인접한 노드들 중에
            if not visited[i]: # 방문하지 않은 노드가 있다면
                queue.append(i)
                visited[i] = True 
    

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현
visited = [ False ] * 9

# DFS 함수 실행
bfs(graph, 1, visited)