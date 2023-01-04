# 정렬 PART3) 카드 정렬하기

n = int(input())   # 숫자 카드 묶음 개수
data = []

for _ in range(n):
    data.append(int(input()))

data.sort()

result = 0
for i in range(len(data)):
    temp = data[i] + data[i+1]
    result += temp
    data[i+1] = temp