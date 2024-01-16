"""
- BOJ 9095: 1,2,3 더하기 (S3)
- https://www.acmicpc.net/problem/9095
"""

n = int(input())

for _ in range(n):
  num = int(input())
  dp = [0] * (num + 1)

  if num == 1:
    print(1)
  elif num == 2:
    print(2)
  elif num == 3:
    print(4)
  else:
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, num+1):
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[num])
