n = int(input())
calender = [0] * 367

"""
배열의 크기를 367로 하는 이유
- 배열의 끝이 1이면 result += row * col이 실행되지 않는다
- 그렇기 때문에 배열의 크기를 하나 더 줘서 0을 만나게 의도해서 계산해준다
"""

# 일정이 몇개있는지를 누적합으로 넣음
for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        calender[i] += 1


row = 0
col = 0
result = 0

for i in range(1, 367):
    if calender[i] != 0:   # 일정이 한개라도 있는 날
        row = max(row, calender[i])   # 최대 row를 구함
        col += 1
    else:   # 일정이 아예 없는 날
        result += row * col
        row, col = 0, 0

print(result)