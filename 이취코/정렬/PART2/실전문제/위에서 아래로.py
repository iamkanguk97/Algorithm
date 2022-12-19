# 정렬 PART2 실전문제) 위에서 아래로

n = int(input())   # N 입력받기
array = []   # 리스트 선언

# 리스트에 입력받은 정수 저장
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)  # 내림차순 정렬
# array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')