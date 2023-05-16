"""
백준 22858 (S3): 원상 복구 (smail)
https://www.acmicpc.net/problem/22858
"""

n, k = map(int, input().split())  # n: 카드의 개수, k: 카드를 섞는 횟수
S = [-1] + list(map(int, input().split()))  # S: K번 카드를 섞은 후 카드의 배치
D = [-1] + list(map(int, input().split()))  # D: 수 배열

for i in range(k):
  temp = [-1] * (n + 1)  # 각 사이클마다 리스트 섞은 결과
  for j in range(1, n + 1):
    idx = D[j]
    temp[idx] = S[j]
  S = temp   # 각 사이클마다 섞은 결과 S에 할당

# 출력
for i in range(1, n + 1):
  print(S[i], end=" ")