# 2798: 블랙잭 (B2)
# n이 100 이하이기 때문에 그냥 for문 사용해도 괜찮을 듯

n, m = map(int, input().split(' '))
cards = list(map(int, input().split()))
maxValue = -1

for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            temp = cards[i] + cards[j] + cards[k]
            if temp == m:
                maxValue = temp
                break
            if temp < m and maxValue < temp:
                maxValue = temp

print(maxValue)