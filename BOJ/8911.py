# BOJ 8911번: 거북이 (S3)

T = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(T):
    moves = input()
    dIdx = 0
    x, y = 0, 0
    min_x, min_y, max_x, max_y = 0, 0, 0, 0

    for move in moves:
        if move == 'L':   # 왼쪽으로 90도 회전
            dIdx += 1
            if dIdx == 4:
                dIdx = 0
        if move == 'R':   # 오른쪽으로 90도 회전
            dIdx -= 1
            if dIdx == -1:
                dIdx = 3
        if move == 'F':   # 앞으로 1칸 이동
            x += dx[dIdx]
            y += dy[dIdx]
        if move == 'B':   # 뒤로 1칸 이동
            x -= dx[dIdx]
            y -= dy[dIdx]
        
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    print(abs(max_x - min_x) * abs(max_y - min_y))
        
    