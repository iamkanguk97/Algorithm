"""
백준 2839 (S4): 설탕 배달 (그리디)
https://www.acmicpc.net/problem/2839
"""

n = int(input())
result = 0

while n >= 0:
    if n % 5 == 0:
      result += n // 5
      break
    else:
       n -= 3
       result += 1

print(result)