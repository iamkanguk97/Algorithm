# 파이썬 기능을 이용한 효율적인 퀵 정렬 소스코드

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]   # PIVOT은 첫 번째 원소로 설정
    _list = array[1:]   # PIVOT을 제외한 원소들 리스트

    left_list = [ x for x in _list if x <= pivot ]   # PIVOT보다 작은 원소들 리스트
    right_list = [ x for x in _list if x > pivot ]   # PIVOT보다 큰 원소들 리스트

    # 분할 한 후에 왼쪽 및 오른쪽 각 부분에서 정렬 진행하고 전체 리스트 반환
    return quick_sort(left_list) + [ pivot ] + quick_sort(right_list)

    
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))