"""
이취코 DFS/BFS PART2: DFS 기본 예제 연습
"""

def dfs(graph, visited, start):
    visited[start] = True   # 해당 노드 방문처리
    print(start, end=' ')
    for node in graph[start]:   # 해당 노드에 인접한 노드들 순회
        if visited[node] == False:   # 인접한 노드에 방문한 적이 없으면 dfs 함수 호출
            dfs(graph, visited, node)

graph = [
    [0],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 7],
    [1, 7]
]

visited = [False] * 9
dfs(graph, visited, 1)