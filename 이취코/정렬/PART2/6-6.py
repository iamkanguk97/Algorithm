# Count sort: 계수 정렬
# (1) 최대값을 찾아서 해당 범위의 크기만큼 리스트 0으로 초기화
# (2) 각 인덱스 번호에 부합하는 숫자 Count 추가
# (3) 각 인덱스 별로 돌면서 Count 별로 숫자 넣기
# 단, 모든 원소의 값이 0보다 크거나 같다고 가정한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
clist = [0] * (max(array) + 1)   # 최대값이 9이기 때문에 0부터 9까지 수용하는 리스트 초기화

# 각 인덱스 번호에 부합하는 숫자에 count 추가
for i in range(len(array)):
    clist[array[i]] += 1

for i in range(len(clist)):
    for _ in range(clist[i]):
        print(i, end=' ')