"""
백준 2839 (S4): 설탕 배달 (DP)
https://www.acmicpc.net/problem/2839
"""

n = int(input())

box = [-1] * 5001
box[3], box[5] = 1, 1

for i in range(6, n+1):
    if box[i-3] != -1:
        box[i] = box[i-3] + 1
    if box[i-5] != -1:
        box[i] = box[i-5] + 1

print(box[n])