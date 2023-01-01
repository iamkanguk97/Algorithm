# 정렬 PART3 - 강욱 Version) 안테나

n = int(input())   # 집의 수
house = list(map(int, input().split()))   # 집의 위치
result = []

for i in range(len(house)):
    d_sum = 0   # 거리 차이의 총합
    for j in range(len(house)):
        d = abs(house[i] - house[j])   # 거리 차이
        d_sum += d
    result.append((house[i], d_sum))   # 결과 저장하는 리스트에 추가

result.sort(key = lambda x: (x[1], x[0]))

print(result[0][0])