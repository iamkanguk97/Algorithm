"""
백준 15650 (S3): N과 M (2)
https://www.acmicpc.net/problem/15650
"""

from itertools import combinations

n, m = map(int, input().split())
numbers = [i+1 for i in range(n)]

result = combinations(numbers, m)
for data in result:
    print(*data)