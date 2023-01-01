# 정렬 PART3 - 책 Version) 안테나
# Solution) 중간값을 선택해야 거리 합이 최소가 될 수 있다!

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = data[(n - 1) // 2]
print(result)