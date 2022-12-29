# 정렬 PART3) 국영수
# 해결 못함... 4개의 조건을 걸어서 한번에 정렬할 수 있는 방법을 몰라서!

n = int(input())
_list = []

for i in range(n):   # N번동안 이름, 국어, 영어, 수학 정보를 입력받아 list에 저장
    name, korean, english, math = input().split()
    _list.append([ name, int(korean), int(english), int(math) ])


_list.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))   # 중요 포인트!! 파이썬에서 한번에 정렬할 수 있는 문법 :(

for i in _list:
    print(i[0])