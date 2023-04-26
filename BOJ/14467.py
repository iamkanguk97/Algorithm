# 백준 14467번: 소가 길을 건너간 이유 1
# https://www.acmicpc.net/problem/14467

data = []
count = 0
N = int(input())

for _ in range(N):
    value = tuple(map(int, input().split()))
    data.append(value)

for i in range(N-1):
    for j in range(i+1, N):
        if data[i][0] == data[j][0]:
            if data[i][1] != data[j][1]:
                count += 1
            break

print(count)