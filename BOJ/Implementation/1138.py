"""
백준 1138 (S2): 한 줄로 서기
https://www.acmicpc.net/problem/1138
"""

n = int(input())   # 사람의 수
data = list(map(int, input().split()))   # 자기보다 큰 사람이 왼쪽에 몇명있는지
check = [0] * n

for i in range(n):
  count = 0   # 왼쪽에 몇명있는지 카운팅
  for j in range(n):
    if check[j] == 0 and count == data[i]:   # 자리가 비워져있고 해당 사람수를 채웠으면
      check[j] = i + 1   # 자리 설정
      break
    elif check[j] == 0:   # 자리가 있는 경우에는 카운팅
      count += 1


print(" ".join(map(str, check)))