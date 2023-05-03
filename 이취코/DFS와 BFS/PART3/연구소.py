# BFS와 DFS PART3 - 연구소
# 삼성전자 SW 역량테스트
# https://www.acmicpc.net/problem/14502

N, M = map(int, input().split()) # N: 세로크기, M: 가로크기
graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y):
    # 지금 있는 곳이 2(바이러스) -> 주변에 확인을 해야됨
    # 사이드가 1 또는 경계면이면 false, 0이면