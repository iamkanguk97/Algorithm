"""
백준 1541 (S2): 잃어버린 괄호
https://www.acmicpc.net/problem/1541
"""

cal = input().split('-')   # - 기준으로 나눠줌
result = []

for c in cal:
  if c.count('+') >= 1:   # +가 1개라도 있으면 계산해줌
    numSum = sum(list(map(int, c.split('+'))))
    result.append(numSum)
  else:
    result.append(int(c))

print(result[0] - sum(result[1:]))