# BOJ 1260번: DFS와 BFS (S2)

def dfs(node):
    print(graph)
    print(node)
    return

def bfs(graph, node):
    return


n, m, v = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(m)]

visited_dfs = []
visited_bfs = []

dfs(v)