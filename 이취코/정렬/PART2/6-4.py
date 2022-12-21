# Quick sort: 퀵 정렬
# 1) PIVOT은 리스트의 맨 왼쪽 숫자를 선택함.
# 2) PIVOT을 제외한 리스트의 맨 왼쪽에서부터 PIVOT보다 큰 수를, 리스트의 맨 오른쪽에서부터 PIVOT보다 작은수를 선택 후 SWAP
# 3) 왼쪽과 오른쪽을 Search하다가 겹치게 되는 경우 PIVOT과 작은수를 SWAP

def quick_sort(array, start, end):
    pivot = start   # 첫 원소는 PIVOT으로 설정
    list_left = pivot + 1   # PIVOT을 제외한 리스트의 맨 왼쪽 IDX
    list_right = end   # PIVOT을 제외한 리스트의 맨 오른쪽 IDX
    
    while True:
        # 왼쪽에서 Search 시작
        while array[list_left] > array[pivot]:   # PIVOT보다 큰 수를 찾을 때 까지
            list_left += 1
        # 오른쪽에서 Search 시작
        while array[list_right] < array[pivot]:   # PIVOT보다 작은 수를 찾을 떄 까지
            list_right -= 1
    



# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# quick_sort(array, 0, len(array)-1)
# print(array)