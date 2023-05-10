"""
백준 2581번: 소수
https://www.acmicpc.net/problem/2581
"""

"""
<소수>
- 소수는 1과 자기 숫자로만 나누어 떨어지는 경우의 숫자를 의미한다.
- 참고로 1은 소수가 아님 (이거 조건 안걸어줘서 틀렸음ㅠ)
"""

M = int(input())
N = int(input())
result = []

for num in range(M, N+1):
    isPrime = True   # 소수인지 확인하는 변수
    if num > 1:
        for n in range(2, num):   # 2부터 자기자신 전까지 반복문을 돌음
            if num % n == 0:   # 나누어 떨어지면 소수가 아님 (1과 자기자신 숫자 빼고)
                isPrime = False
                break
        if isPrime:
            result.append(num)


# 두 숫자 사이에 소수가 없을 경우 -1 출력
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))