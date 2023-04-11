# DFS 기본 코드 (깊이 우선 탐색)

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end = ' ') # 방문한 노드 출력

    # 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # 해당 노드를 방문하지 않았으면?
            dfs(graph, i, visited) # 노드를 방문해서 똑같이 DFS 과정 진행

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
dfs(graph, 1, visited)