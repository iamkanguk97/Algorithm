"""
프로그래머스 LV1: 크레인 인형뽑기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/64061
2019년도 카카오 개발자 겨울 인턴십
"""

"""
[0,0,0,0,0]
[0,0,1,0,3]
[0,2,5,0,1]
[4,2,4,4,2]
[3,5,1,3,1]
"""

def solution(board, moves):
    count = 0
    bucket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:   # 빈칸이 아니고 인형이 있으면               
                bucket.append(board[i][move-1])   # 바구니에 담음
                board[i][move-1] = 0   # 빈칸 처리
                                
                # 바구니에 담고 터뜨릴게 있는지 확인
                if len(bucket) >= 2:
                    if bucket[len(bucket)-1] == bucket[len(bucket)-2]:
                        for _ in range(2):
                            bucket.pop()
                        count += 2
                
                break
    
    return count