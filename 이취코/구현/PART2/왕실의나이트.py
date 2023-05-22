"""
이취코 구현 PART2: 왕실의 나이트
난이도: 1
"""

result = 0
position = input()
row = int(position[1])
col = int(ord(position[0])) - int(ord('a')) + 1
direction = [
    # 수평으로 2칸 이동후 수직으로 1칸이동
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    # 수직으로 2칸 이동후 수평으로 1칸이동
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1)
]

for d in direction:
    # 좌표 이동
    nrow = row + d[0]
    ncol = col + d[1]

    # 체스판 위에 위치할 수 있으면 경우의수 추가
    if 1 <= nrow <= 8 and 1 <= ncol <= 8:
        result += 1


print(result)