"""
프로그래머스 LV2: N-Queen (실패)
https://school.programmers.co.kr/learn/courses/30/lessons/12952
"""

def queen(x, n, col):
    # row가 끝까지 갔으면 성공
    if x == n:
        return 1

    count = 0
    for i in range(n):   # x번째 줄(행)의 각 열
        col[x] = i   # ex) col[0] = 0 -> 0번째 줄의 0번째 열에 Queen이 놓여져 있다는 뜻
        for j in range(x):
            if col[j] == col[x]:   # 같은 열에 Queen이 위치한 경우
                break
            if abs(col[j] - col[x]) == x - j:   # 대각선에 Queen이 위치한 경우
                break
        else:
            count += queen(x+1, n, col)
    
    return count
            
    
def solution(n):
    col = [0] * n   # row의 index를 담기 위한 리스트
    answer = queen(0, n, col)   # 0: 세로축의 시작점, n: 맵의 크기, col은 row의 index를 담기위한 리스트
    return answer