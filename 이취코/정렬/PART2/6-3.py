# Insertion sort: 삽입 정렬

# CASE 1) 맨땅에 헤딩으로 작성한 코드. 삽입 정렬의 장점을 살리지 못한 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    curr_idx = i
    for j in range(i-1, -1, -1):
        if array[curr_idx] < array[j]:
            array[curr_idx], array[j] = array[j], array[curr_idx]
            curr_idx = j

print(array)

# CASE 2) 삽입 정렬은 전부다 비교할 필요 없다. 현재 value보다 작은 값을 만나게 되면 break로 반복문 탈출시켜준다!
_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(_array)):
    for j in range(i, 0, -1):
        if _array[j] < _array[j-1]:
            _array[j], _array[j-1] = _array[j-1], _array[j]
        else:
            break

print(_array)