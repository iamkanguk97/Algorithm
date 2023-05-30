"""
백준 15650 (S3): N과 M (1)
https://www.acmicpc.net/problem/15649
"""

from itertools import permutations

n, m = map(int, input().split())
numbers = [i+1 for i in range(n)]

result = permutations(numbers, m)
for data in result:
    print(*data)