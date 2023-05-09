"""
백준 11650: 좌표 정렬하기
https://www.acmicpc.net/problem/11650
"""

N = int(input())   # 2차원 평면 위의 점 개수
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x:(x[0], x[1]))   # lambda를 사용해서 정렬기준 만족

# 출력
for data in lst:
    print(*data)