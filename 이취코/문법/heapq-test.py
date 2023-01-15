# 파이썬에서는 힙 기능을 위해 heapq 라이브러리 지원함 (우선순위 큐 - 최소 힙)
# 시간복잡도 O(NlogN)에 오름차순 정렬이 가능하다 (최소 힙의 최상단 원소는 항상 가장 작은 원소)
# heapq.heappush, heapq.heappop

import heapq

def heapsort(iterable):
    heap = []
    result = []

    for value in iterable:   # 모든 원소를 차례대로 heap에 넣음 -> 넣을때는 따로 정렬이 되진 않음
        heapq.heappush(heap, value)

    # heap에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    
    return result

heap_result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(heap_result)


# 파이썬에서는 최대 힙을 제공하지 않음.
# heapq를 통해 최대 힙을 구현해야 한다면 원소의 부호를 임시로 바꾸는 방법을 사용한다.
# 힙에 원소를 삽입하기 전에 부호를 반대로 바꾸었다가 꺼낼 때 부호를 다시 바꿔준다 -> 내림차순 힙 정렬 구현
def _heapsort(iterable):
    heap = []
    result = []

    for value in iterable:   # 모든 원소를 차례대로 heap에 넣음
        heapq.heappush(heap, -value)

    # heap에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(heap)):
        result.append(-heapq.heappop(heap))
    
    return result

heap_result_ = _heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(heap_result_)