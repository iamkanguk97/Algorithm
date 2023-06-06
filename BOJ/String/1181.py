"""
백준 1181 (S5): 단어 정렬
https://www.acmicpc.net/problem/1181
"""

n = int(input())
data = list(set([input() for _ in range(n)]))   # 중복제거를 위해 set을 적용
data.sort(reverse=False, key=lambda x: (len(x), x))   # 문자열 길이 -> 사전순

for d in data:
  print(d)
