"""
이취코 구현 PART2: 시각
난이도: 1
"""

"""
n = 5이면
00시 00분 00초 ~ 05시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 확인
"""

n = int(input())
result = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            time = str(h) + str(m) + str(s)
            if time.count('3') > 0:
                result += 1


print(result)