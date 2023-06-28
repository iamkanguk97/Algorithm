"""
백준 1697: 숨바꼭질
https://www.acmicpc.net/problem/1697
"""

"""
ex) 5->17로 가는 길
5->10->9->18->17

- 곱하기
- 더하기
- 빼기
"""

from collections import deque

def bfs(n):
    queue = deque([n])
    while queue:
        node = queue.popleft()
        if node == k:
            return visited[node]
        for next_node in (node-1, node+1, node*2):
            if 0 <= next_node <= 100000 and not visited[next_node]:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)
            

n, k = map(int, input().split())
visited = [0] * 100001
print(bfs(n))