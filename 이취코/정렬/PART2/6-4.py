# Quick sort: 퀵 정렬
# 1) PIVOT은 리스트의 맨 왼쪽 숫자를 선택함.
# 2) PIVOT을 제외한 리스트의 맨 왼쪽에서부터 PIVOT보다 큰 수를, 리스트의 맨 오른쪽에서부터 PIVOT보다 작은수를 선택 후 SWAP
# 3) 왼쪽과 오른쪽을 Search하다가 겹치게 되는 경우 PIVOT과 작은수를 SWAP

def quick_sort(array, start, end):
    if start >= end:   # 리스트의 원소가 1개인 경우 함수 종료
        return

    pivot = start
    lt = start + 1   # 리스트 왼쪽 원소 (PIVOT보다 1칸 오른쪽)
    rt = end   # 리스트 오른쪽 원소 (맨 끝)

    # 원소 탐색 시작
    while lt <= rt:
        while lt <= end and array[pivot] >= array[lt]:   # PIVOT보다 큰 데이터 탐색
            lt += 1
        while rt > start and array[pivot] <= array[rt]:   # PIVOT보다 작은 데이터 탐색
            rt -= 1

        if lt > rt:   # left와 right가 교차된 순간에는 right와 pivot을 swap
            array[rt], array[pivot] = array[pivot], array[rt]
        else:
            array[lt], array[rt] = array[rt], array[lt]


    # 분할 이후 왼쪽 리스트와 오른쪽 리스트 quick_sort 진행
    quick_sort(array, start, rt - 1)
    quick_sort(array, rt + 1, end)

    
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array)-1)
print(array)