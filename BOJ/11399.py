# 백준 11399번: ATM
# https://www.acmicpc.net/problem/11399

N = int(input())
time = sorted(list(map(int, input().split())))
result = 0

for i in range(N):
    for j in range(i+1):
        result += time[j]

print(result)