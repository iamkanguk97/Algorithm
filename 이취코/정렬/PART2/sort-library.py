# 정렬 라이브러리 소스코드
# sorted는 반환값이 있고, sort 메서드는 해당 변수에 직접 접근해서 변화를 준다.
# sorted와 sort 모두 key 매개변수를 사용할 수 있는데 key는 함수를 넣어주면 된다.
# 기본적으로 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장한다. 심지어 직접 퀵 정렬을 구현할 때 보다 효율적이다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted
result = sorted(array)
print(result)

# sort
array.sort()
print(array)

# sorted와 sort with key parameter
def setting(arr):
    return arr[1]

_array = [('바나나', 2), ('사과', 5), ('당근', 3)]
_result = sorted(_array, key=setting)
print(_result)