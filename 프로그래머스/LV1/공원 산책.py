"""
프로그래머스 LV1: 공원 산책
https://school.programmers.co.kr/learn/courses/30/lessons/172928
"""

def makeMatrixAndStart(park):
    matrix = []
    start_x, start_y = None, None
    
    for idx, p in enumerate(park):
        _p = list(p)
        if _p.count('S') == 1:
            start_x, start_y = idx, _p.index('S')
        matrix.append(_p)
    
    return matrix, start_x, start_y
    

def solution(park, routes):
    direction = ['N', 'W', 'S', 'E']
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    matrix, start_x, start_y = makeMatrixAndStart(park)
    width, height = len(matrix[0]), len(matrix)
    
    for route in routes:
        d, count = route.split(' ')
        d_idx = direction.index(d)
        check = False
        temp_x, temp_y = start_x, start_y   # 임시 저장
        
        for _ in range(int(count)):
            start_nx = start_x + dx[d_idx]
            start_ny = start_y + dy[d_idx]
            
            if (start_nx < 0 or start_ny < 0 or start_nx >= height or start_ny >= width) or matrix[start_nx][start_ny] == 'X':
                check = True
                break
            else:
                start_x, start_y = start_nx, start_ny
                
        if check == True:
            start_x, start_y = temp_x, temp_y
            
    return [start_x, start_y]
        