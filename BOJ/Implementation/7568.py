"""
백준 7568 (S5): 덩치
https://www.acmicpc.net/problem/7568
"""

n = int(input())  # 사람의 수
info = [tuple(map(int, input().split())) for _ in range(n)]  # 몸무게와 키
rank = []   # 덩치 등수 저장

for i in range(n):
  temp = 1
  for j in range(n):
    if i == j:
      continue
    else:
      if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
        temp += 1
  rank.append(temp)

for r in rank:
  print(r, end=" ")