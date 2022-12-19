# Selection sort: 선택 정렬

# CASE 1) 파이썬 SWAP 코드 모르고 작성
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp


# CASE 2) 파이썬 SWAP 코드 적용
_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(_array)):
    min_idx = i
    for j in range(i+1, len(_array)):
        if _array[min_idx] > _array[j]:
            min_idx = j
    # FOR문을 전부 거치고 난 후 값이 제일 앞으로 갈 IDX를 결정한 후 마지막에 SWAP
    _array[i], _array[min_idx] = _array[min_idx], _array[i]   # SWAP 코드


print(array)
print(_array)