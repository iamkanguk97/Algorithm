# Algorithm

[![Solved.ac Profile](http://mazassumnida.wtf/api/generate_badge?boj=iamkangukii)](https://solved.ac/iamkangukii)

- [이것이 취업을 위한 코딩테스트다 with 파이썬](https://github.com/ndb796/python-for-coding-test)
- [Baekjoon Online Judge](https://www.acmicpc.net/)
- [코딩테스트 대비 문제집 with Baekjoon](https://github.com/tony9402/baekjoon)
- [Programmers](https://school.programmers.co.kr/learn/challenges?order=recent&levels=1)

## Plan

- `✊ 코딩테스트를 합격하는 그날까지! 꾸준하게 아자아자 ✊`
- `🤓 네이버 부스트캠프 8기 코딩테스트 준비중! 🤓 (06/19)`

## 코딩테스트 문제 풀이 회고

[코딩테스트 문제 풀이 회고 시리즈 Velog](https://velog.io/@kangukii97/series/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8)

---

## Python 코딩테스트 문법 정리

코딩테스트 문제를 풀어보면서 몰랐던 개념들을 정리!

> 좋은 자료를 공유해주신 [Covenant](https://covenant.tistory.com/141)님 감사합니다!<br>
> 제가 문제 풀면서 어려웠던 부분 정리랑 Covenant님의 용감하게 시작하는 코딩테스트 시리즈를 참고해서 작성했습니다 :)

### 1. 나누어서 입력받기 + 입/출력 가속

#### 나누어서 입력받기

```python
a, b = map(int, input().split())
```

map을 통해 각 변수에 값을 할당해줍니다! 이 때 split을 통해 기준점을 정해서 나눠줍니다.

#### 입/출력 가속

입력값이 많은 문제의 경우에는 input() 함수를 사용하면 pypy3으로 제출해도 시간초과가 나오는 경우가 있습니다. 이 경우에는 아래 코드로 대체하면 빠르게 입력받을 수 있습니다.<br>
(참고 - stdout.write 할 때 문자열만 출력할 수 있습니다)

```python
import sys
N = int(sys.stdin.readline())
sys.stdout.write(str(N))
```

하지만 sys.stdout이라고 코드를 적는건 너무나 귀찮습니다! 그렇기 때문에 더욱 더 간단한 방법이 있습니당😃

```python
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
```

위와 같이 코드를 맨 위에 작성하게 되면 평소에 print 함수를 호출하듯이 사용하면 됩니다.<br>
하지만 위처럼 사용하면 오른쪽에 개행문자가 붙게 됩니다. 개행문자를 제거해주고 싶으면 `.rstrip()`을 붙여주면 됩니다.<br>
참고로 split을 사용하거나 int로 형변환 하는 경우에는 rstrip을 안붙여도 됩니다!

### 2. 배열 입출력

#### 입력 (CASE 1)

```
3
1 2 3
4 5 6
7 8 9
```

위와 같이 입력예시가 주어졌다면 아래 코드와 같이 한줄로 처리가 가능하다!

```python
result = [list(map(int, input().split())) for _ in range(int(input()))]
```

#### 입력 (CASE 2)

```
4 10 20 30 40
3 7 5 12
3 125 15 25
```

다음과 같이 한 줄에 첫 숫자는 개수, 다음에는 n개의 수를 입력받는 경우입니다.

```python
N, *arr = map(int, input().split())
```

이렇게 arr앞에 `*`을 붙이게 되면 뒤에 이어서 나오는 값이 arr 배열에 저장됩니다.

#### 출력 (CASE 1)

```python
arr = [1, 2, 3, 4] # -> 1234
```

arr 배열을 주석과 같이 `1234`로 출력하고 싶다.

```python
print("".join(map(str, arr)))
```

map 함수를 사용해서 arr에 저장되어 있는 정수의 값을 string으로 타입을 변환하고 `"".join()`을 사용해서 공백없이 값을 출력할 수 이씀!

#### 출력 (CASE 2)

```python
arr = [1, 2, 3, 4] # -> 1 2 3 4
```

이번에는 붙혀서가 아닌 대괄호와 쉼표만 없애서 출력하고 싶슴다!

```python
print(*arr)
```

`*`을 붙이면 아주 간단하게 해결이 가능하다.<br>
진짜 완전 핵간단함... 몰랐을 때는 for문으로 했는데 이걸 알고나니까 진짜 완전 편하다!
(물론 반복문으로 출력해도 되긴함)

### 3. 문자열

#### 문자열 거꾸로

문자열을 ABCD에서 DCBA로 바꾸려면 어떻게 할까요오?

```python
str = 'ABCD'
print(str[::-1])
```

#### 문자열 <-> 아스키코드

```python
ord() # 문자를 아스키코드로 변환하는 함수
chr() # 아스키코드를 문자로 변환하는 함수
```

기업 코딩테스트에서는 출제빈도가 낮은 유형이라고는 하니 참고만 하자!

### 4. 배열

#### 배열 초기화

**배열 초기화는 코딩테스트에서 아주아주아주아주 많이 사용하기 때문에 꼭 기억할 것!**

```python
# 입력예시: 3 5

N, M = map(int, input().split())
arr = [[0] * N for _ in range(M)]
```

`여기서 하나 꿀팁으로는 배열의 가로 세로를 각각 N과 M으로 설정하면 좋음!` <br>
문제마다 가로와 세로를 반대로 주는 경우가 있는데 우리가 N을 가로, M을 세로로 딱 정해버리면 헷갈리지 않을 수 있음.

#### 배열의 원소를 거꾸로

```python
arr.reverse()
```

#### 배열 원소 개수

```python
list.count(찾는 값)
str.count(찾는 값)
```

배열 뿐만 아니라 문자열 형태에서도 찾는 값이 몇 개있는지 확인할 수 있습니다.

#### 원소 중복 제거

```python
result = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ]
result = list(set(result))
```

set은 중복없이 유일하다는 속성이 있다. 그래서 배열을 set으로 변경해줌으로서 중복값을 없애고 다시 list로 저장하는 것이다!

```python
result2 = [[1,2], [1,2], [1]]
```

만약에 위와같이 2차원 리스트가 있을때 중복값을 없애고 싶으면 어케할까용?

```python
print(list(set(map(tuple, result2))))
```

#### 배열 정렬

오름차순 또는 내림차순으로 정렬하려면 다음과 같이 사용하면 됩니당

```python
arr.sort()   # 오름차순
arr.sort(reverse=True)   # 내림차순
```

`만약 배열의 원소가 각각 한개가 아니라 리스트라면 어떻게 할까요?`

```python
arr.sort(key=lambda x:(x[0], x[1]))
```

이처럼 람다를 사용해주면 됩니다. **정렬 기준은 첫 번째 좌표(x[0])가 증가하는 순으로 정렬이 되고, x[0]이 같으면 두 번째 좌표인 x[1]을 기준으로 정렬을 하게 되는 코드입니다.**

해당 부분은 [백준 11650번 좌표 정렬하기](https://www.acmicpc.net/problem/11650)를 lambda를 사용해서 풀어보면 확실하게 감을 잡으실 수 있을 거 같습니다!

**참고로 lambda를 사용해서 내림차순 정렬을 하고 싶으면 `-x[0]` 과 같은 방법으로 작성해주시면 됩니다!!**

### 5. 파이썬에서의 삼항 연산자

파이썬에서는 삼항 연산자를 다음과 같이 사용함다

```python
[True 조건] if 조건 else [False 조건]

if a > b:
    res = a
else:
    res = b

# 위의 코드를 이렇게 간단하게!!
res = a if a > b else b
```